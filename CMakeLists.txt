cmake_minimum_required(VERSION 2.8.3)
project(motors)

## Find catkin and any catkin packages
# Do not just add this to your CMakeLists.txt, modify the existing text to add message_generation before the closing parenthesis
find_package(catkin REQUIRED COMPONENTS
   roscpp
   rospy
   std_msgs
   message_generation
   roslaunch
)

add_message_files(
  FILES
  MotorMsg.msg
)

add_service_files(
  FILES
  MoveMotor.srv
  Torque.srv
  TorqueAll.srv
)

generate_messages(
  DEPENDENCIES
  std_msgs
)

## Declare a catkin package
catkin_package(
   CATKIN_DEPENDS message_runtime
)


## Build talker and listener
include_directories(include ${catkin_INCLUDE_DIRS})

install(DIRECTORY launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

roslaunch_add_file_check(launch)
