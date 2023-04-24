from as2_python_api.mission_interpreter.mission import Mission, MissionItem
from as2_msgs.msg import YawMode

from std_msgs.msg import String
from mutac_msgs.msg import Plan

from rclpy import qos
import rclpy.executors

import rclpy
from rclpy.node import Node
from rclpy.publisher import Publisher

import sys
import threading
from time import sleep

from typing import List

class MissionTransmitter(Node):
    def __init__(self, n_drones, namespace):
        super().__init__("MissionTransmitter")
        self.keep_running = True

        self.n_drones = n_drones
        self.namespace = namespace

        self.mission_pubs : List[Publisher] = list()

        self.plan_sub = self.create_subscription(Plan, "/mutac/planned_paths", self.path_callback, qos.QoSProfile(reliability=qos.ReliabilityPolicy.RELIABLE, depth=10))

        for i in range(self.n_drones):
            mission_pub_name = str("/" + self.namespace + str(i) + "/mission")
            self.mission_pubs.append(self.create_publisher(String, mission_pub_name, qos.QoSProfile(reliability=qos.ReliabilityPolicy.RELIABLE, depth=10)))
        
        self.__executor = rclpy.executors.SingleThreadedExecutor()
        self.__executor.add_node(self)

        self.t_spin_node = threading.Thread(target=self.spin_node)
        self.t_spin_node.start()

    #TODO HACER EL HOVER EN EL DRONE EVENTS CALLBACK

    def path_callback(self, msg : Plan):
        self.get_logger().info("Got plan")
        missions : List[Mission] = list()
        for d in range(n_drones):
            target = self.namespace + str(d)
            missions.append(Mission(target=target, verbose=False))
            # json_msg = missions[d].json()
            # self.mission_pubs[d].publish(String(data=json_msg))
            missions[d].plan.append(MissionItem(behavior='takeoff', args={
                'height': 1.0,
                'speed': 0.5,
                'wait': True
            }))

        for p in msg.paths:
            n = p.identifier.natural
            for point in p.points[1:]:
                missions[n].plan.append(MissionItem(behavior='go_to', args={
                    '_x': point.point.x, '_y': point.point.y, '_z': point.point.z,
                    'speed': 0.5,
                    'yaw_mode': YawMode.FIXED_YAW, 'yaw_angle': 0.00,
                    'wait': True
                }))
            missions[n].plan.append(MissionItem(behavior='land', args={
                'speed': 0.5,
                'wait': True
            }))
            json_msg = missions[n].json()
            self.mission_pubs[n].publish(String(data=json_msg))
            print(json_msg)


    def spin_node(self):
        while self.keep_running and rclpy.ok():
            self.__executor.spin_once(timeout_sec=0)
            sleep(0.05)

    def shutdown(self):
        self.keep_running = False
        self.destroy_client(self.plan_cli)

if __name__ == '__main__':
    rclpy.init()

    if(len(sys.argv) < 3):
        print("Usage: python3 mission_transmitter.py n_drones namespace")
        exit(-1)

    n_drones = int(sys.argv[1])
    uav_namespace = str(sys.argv[2])

    mission_transmitter = MissionTransmitter(n_drones, uav_namespace)