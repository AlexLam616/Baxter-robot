# Install script for directory: /home/alex/workspace/src/learning_ros_noetic/Part_5/baxter/baxter_jnt_traj_ctlr_client

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/alex/workspace/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/baxter_jnt_traj_ctlr_client/baxter_jnt_traj_ctlr_client_pre_pose" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/baxter_jnt_traj_ctlr_client/baxter_jnt_traj_ctlr_client_pre_pose")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/baxter_jnt_traj_ctlr_client/baxter_jnt_traj_ctlr_client_pre_pose"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/baxter_jnt_traj_ctlr_client" TYPE EXECUTABLE FILES "/home/alex/workspace/devel/lib/baxter_jnt_traj_ctlr_client/baxter_jnt_traj_ctlr_client_pre_pose")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/baxter_jnt_traj_ctlr_client/baxter_jnt_traj_ctlr_client_pre_pose" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/baxter_jnt_traj_ctlr_client/baxter_jnt_traj_ctlr_client_pre_pose")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/baxter_jnt_traj_ctlr_client/baxter_jnt_traj_ctlr_client_pre_pose"
         OLD_RPATH "/home/alex/workspace/devel/lib:/opt/ros/noetic/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/baxter_jnt_traj_ctlr_client/baxter_jnt_traj_ctlr_client_pre_pose")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/baxter_jnt_traj_ctlr_client/baxter_jnt_traj_ctlr_client_home" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/baxter_jnt_traj_ctlr_client/baxter_jnt_traj_ctlr_client_home")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/baxter_jnt_traj_ctlr_client/baxter_jnt_traj_ctlr_client_home"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/baxter_jnt_traj_ctlr_client" TYPE EXECUTABLE FILES "/home/alex/workspace/devel/lib/baxter_jnt_traj_ctlr_client/baxter_jnt_traj_ctlr_client_home")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/baxter_jnt_traj_ctlr_client/baxter_jnt_traj_ctlr_client_home" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/baxter_jnt_traj_ctlr_client/baxter_jnt_traj_ctlr_client_home")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/baxter_jnt_traj_ctlr_client/baxter_jnt_traj_ctlr_client_home"
         OLD_RPATH "/home/alex/workspace/devel/lib:/opt/ros/noetic/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/baxter_jnt_traj_ctlr_client/baxter_jnt_traj_ctlr_client_home")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/baxter_jnt_traj_ctlr_client/baxter_jnt_traj_ctlr_client_Jacobian_move" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/baxter_jnt_traj_ctlr_client/baxter_jnt_traj_ctlr_client_Jacobian_move")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/baxter_jnt_traj_ctlr_client/baxter_jnt_traj_ctlr_client_Jacobian_move"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/baxter_jnt_traj_ctlr_client" TYPE EXECUTABLE FILES "/home/alex/workspace/devel/lib/baxter_jnt_traj_ctlr_client/baxter_jnt_traj_ctlr_client_Jacobian_move")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/baxter_jnt_traj_ctlr_client/baxter_jnt_traj_ctlr_client_Jacobian_move" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/baxter_jnt_traj_ctlr_client/baxter_jnt_traj_ctlr_client_Jacobian_move")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/baxter_jnt_traj_ctlr_client/baxter_jnt_traj_ctlr_client_Jacobian_move"
         OLD_RPATH "/home/alex/workspace/devel/lib:/opt/ros/noetic/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/baxter_jnt_traj_ctlr_client/baxter_jnt_traj_ctlr_client_Jacobian_move")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/alex/workspace/build/learning_ros_noetic/Part_5/baxter/baxter_jnt_traj_ctlr_client/catkin_generated/installspace/baxter_jnt_traj_ctlr_client.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/baxter_jnt_traj_ctlr_client/cmake" TYPE FILE FILES
    "/home/alex/workspace/build/learning_ros_noetic/Part_5/baxter/baxter_jnt_traj_ctlr_client/catkin_generated/installspace/baxter_jnt_traj_ctlr_clientConfig.cmake"
    "/home/alex/workspace/build/learning_ros_noetic/Part_5/baxter/baxter_jnt_traj_ctlr_client/catkin_generated/installspace/baxter_jnt_traj_ctlr_clientConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/baxter_jnt_traj_ctlr_client" TYPE FILE FILES "/home/alex/workspace/src/learning_ros_noetic/Part_5/baxter/baxter_jnt_traj_ctlr_client/package.xml")
endif()

