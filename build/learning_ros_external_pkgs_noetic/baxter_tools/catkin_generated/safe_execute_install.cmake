execute_process(COMMAND "/home/alex/workspace/build/learning_ros_external_pkgs_noetic/baxter_tools/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/alex/workspace/build/learning_ros_external_pkgs_noetic/baxter_tools/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
