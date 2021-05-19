# generated from catkin/cmake/template/pkg.context.pc.in
CATKIN_PACKAGE_PREFIX = ""
PROJECT_PKG_CONFIG_INCLUDE_DIRS = "${prefix}/include".split(';') if "${prefix}/include" != "" else []
PROJECT_CATKIN_DEPENDS = "roscpp;baxter_fk_ik;arm7dof_fk_ik;arm7dof_traj_as;ur_fk_ik;irb120_fk_ik;joint_space_planner;std_msgs;geometry_msgs;actionlib;message_runtime;baxter_trajectory_streamer;tf;xform_utils;simple_baxter_gripper_interface".replace(';', ' ')
PKG_CONFIG_LIBRARIES_WITH_PREFIX = "-lbaxter_cartesian_planner;-larm7dof_cartesian_planner;-lur10_cartesian_planner;-lcart_motion_commander".split(';') if "-lbaxter_cartesian_planner;-larm7dof_cartesian_planner;-lur10_cartesian_planner;-lcart_motion_commander" != "" else []
PROJECT_NAME = "cartesian_planner"
PROJECT_SPACE_DIR = "/home/alex/workspace/install"
PROJECT_VERSION = "0.0.0"
