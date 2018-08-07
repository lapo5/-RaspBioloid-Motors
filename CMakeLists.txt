cmake_minimum_required(VERSION 2.8.3)
project(motors)

find_package(catkin REQUIRED COMPONENTS
  rospy
  roslaunch
  motors_msgs
  motors_srvs
  dynamixel_sdk
)

catkin_package(
   CATKIN_DEPENDS rospy roslaunch motors_msgs motors_srvs dynamixel_sdk
)

include_directories(include ${catkin_INCLUDE_DIRS})

install(DIRECTORY launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

roslaunch_add_file_check(launch)
