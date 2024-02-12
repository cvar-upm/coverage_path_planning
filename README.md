# A multi-UAV system for coverage path planning applications with in-flight re-planning capabilities
This repository is part of **Aerostack2**[[1]](#1), and contains the code for the Powell **BINPAT**[[2]](#2).  method for planning multi-area coverage trajectories with multiple UAVs. Its main contribution is the control architecture that allows estimating the status of the mission through monitoring the status of the aircraft; so that if an aircraft is lost during the flight, the system replans the mission with the remaining aircraft and completes the flight.
Details of this approach are found in [[3]](#3).
Additionally, the configuration has been uploaded for testing in simulated environments in Gazebo, and real environments using Crazyfly UAVs and the Optitrack motion capture system.

## References
<a id="1">[1]</a> 
Fernandez-Cortizas, M., Molina, M., Arias-Perez, P., Perez-Segui, R., Perez-Saura, D., & Campoy, P. (2023). Aerostack2: A Software Framework for Developing Multi-robot Aerial Systems. arXiv preprint arXiv:2303.18237.
<a id="2">[2]</a> 
Luna, M. A., Ale Isaac, M. S., Ragab, A. R., Campoy, P., Flores Peña, P., & Molina, M. (2022). Fast multi-uav path planning for optimal area coverage in aerial sensing applications. Sensors, 22(6), 2297.
<a id="3">[3]</a> 
Luna, M. A., Molina, M., Da-Silva-Gomez, R., Melero-Deza, J., Arias-Perez, P., & Campoy, P. (2023). A multi-UAV system for coverage path planning applications with in-flight re-planning capabilities. Authorea Preprints.

