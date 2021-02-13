cmake_minimum_required(VERSION 3.0.2)
project(ros_gsplines)
find_package(catkin REQUIRED COMPONENTS 
    rospy
    roscpp
    std_msgs
    message_generation)
catkin_python_setup()
catkin_package(CATKIN_DEPENDS message_runtime)
include_directories(${catkin_INCLUDE_DIRS})
add_message_files(
  FILES
  jointGSplineTrajectory.msg
)
generate_messages(
  DEPENDENCIES
  std_msgs
)
