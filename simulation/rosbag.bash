#!/bin/bash
ros2 bag record -o $1 /tf /tf_static /clock /planner/visualization/drone_sim_0/path_left /planner/visualization/drone_sim_0/covered_path /planner/visualization/drone_sim_1/path_left /planner/visualization/drone_sim_1/covered_path /planner/visualization/drone_sim_2/path_left /planner/visualization/drone_sim_2/covered_path
