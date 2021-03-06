// block_grabber_action_client: minimalist client
// wsn, November, 2016
// use with object_grabber action server called "objectGrabberActionServer"
// in file object_grabber_as.cpp

//client gets gripper ID from param server
// gets grasp strategy options from manip_properties(gripper_ID,object_ID)
// two primary fncs:
//   **   object_grab(object_id, object_pickup_pose, grasp_strategy, approach_strategy, depart_strategy)
//  **   object_dropoff(object_id, object_destination_pose, grasp_strategy, dropoff_strategy, depart_strategy)
//      have default args for grasp_strategy, depart_strategy, ...
//       default is grab from above, approach and depart from above
//      grasp strategy implies a grasp transform--to be used by action service for planning paths
//       all coords expressed as object frame w/rt named frame--which must have a 
//        kinematic path to system_ref_frame (e.g. simply use system_ref_frame)


#include<ros/ros.h>
#include <actionlib/client/simple_action_client.h>
#include <actionlib/client/terminal_state.h>
#include <object_grabber/object_grabberAction.h>
#include <Eigen/Eigen>
#include <Eigen/Dense>
#include <Eigen/Geometry>
#include <xform_utils/xform_utils.h>
#include <object_manipulation_properties/object_ID_codes.h>
#include<generic_gripper_services/genericGripperInterface.h>

using namespace std;
XformUtils xformUtils; //type conversion utilities

int g_object_grabber_return_code;

void objectGrabberDoneCb(const actionlib::SimpleClientGoalState& state,
        const object_grabber::object_grabberResultConstPtr& result) {
    ROS_INFO(" objectGrabberDoneCb: server responded with state [%s]", state.toString().c_str());
    g_object_grabber_return_code = result->return_code;
    ROS_INFO("got result output = %d; ", g_object_grabber_return_code);
}


//test fnc to specify object pick-up and drop-off frames;
//should get pick-up frame from perception, and drop-off frame from perception or task

void set_example_object_frames(geometry_msgs::PoseStamped &object_poseStamped,
        geometry_msgs::PoseStamped &object_dropoff_poseStamped) {
    //hard code an object pose; later, this will come from perception
    //specify reference frame in which this pose is expressed:
    //will require that "system_ref_frame" is known to tf
    object_poseStamped.header.frame_id = "system_ref_frame"; //set object pose; ref frame must be connected via tf
    object_poseStamped.pose.position.x = -0.85;
    object_poseStamped.pose.position.y = 0.85;
    object_poseStamped.pose.position.z = 0.5622; //-0.125; //pose w/rt world frame
    object_poseStamped.pose.orientation.x = 0;
    object_poseStamped.pose.orientation.y = 0;
    object_poseStamped.pose.orientation.z = 0.0;
    object_poseStamped.pose.orientation.w = 1;
    object_poseStamped.header.stamp = ros::Time::now();

    object_dropoff_poseStamped = object_poseStamped; //specify desired drop-off pose of object
    object_dropoff_poseStamped.pose.position.x = 1;
    object_dropoff_poseStamped.pose.position.y = 0;
    object_dropoff_poseStamped.pose.position.z = 0.793; 
}

int main(int argc, char** argv) {
    ros::init(argc, argv, "example_object_grabber_action_client");
    ros::NodeHandle nh;
    double dt_wait = 0.5; //check status this often
    double wait_time;
    const double MAX_WAIT_TIME = 30.0; // 30-second watchdog
    ros::Duration sleeper(dt_wait);

    int object_id = ObjectIdCodes::COKE_CAN_UPRIGHT; //choose object of interest


    object_grabber::object_grabberGoal object_grabber_goal;
    geometry_msgs::PoseStamped object_pickup_poseStamped;
    geometry_msgs::PoseStamped object_dropoff_poseStamped;
    //specify object pick-up and drop-off frames using simple test fnc
    //more generally, pick-up comes from perception and drop-off comes from task
    set_example_object_frames(object_pickup_poseStamped, object_dropoff_poseStamped);

    actionlib::SimpleActionClient<object_grabber::object_grabberAction> object_grabber_ac("object_grabber_action_service", true);

    ROS_INFO("waiting for server: ");
    bool server_exists = false;
    while ((!server_exists)&&(ros::ok())) {
        server_exists = object_grabber_ac.waitForServer(ros::Duration(0.5)); // 
        ros::spinOnce();
        ros::Duration(0.5).sleep();
        ROS_INFO("retrying...");
    }
    ROS_INFO("connected to object_grabber action server"); // if here, then we connected to the server; 


    bool finished_before_timeout;
    ROS_INFO("sending test code: ");
    object_grabber_goal.action_code = object_grabber::object_grabberGoal::TEST_CODE;
    object_grabber_ac.sendGoal(object_grabber_goal, &objectGrabberDoneCb);
    finished_before_timeout = object_grabber_ac.waitForResult(ros::Duration(30.0));
    if (!finished_before_timeout) {
        ROS_WARN("giving up waiting on result ");
        return 1;
    }

    //move to waiting pose
    ROS_INFO("sending command to move to waiting pose");
    object_grabber_goal.action_code = object_grabber::object_grabberGoal::MOVE_TO_WAITING_POSE;
    object_grabber_ac.sendGoal(object_grabber_goal, &objectGrabberDoneCb);
    finished_before_timeout = object_grabber_ac.waitForResult(ros::Duration(30.0));
    if (!finished_before_timeout) {
        ROS_WARN("giving up waiting on result ");
        return 1;
    }



    ROS_INFO("sending a grab-object command");
    object_grabber_goal.action_code = object_grabber::object_grabberGoal::GRAB_OBJECT; //specify the action to be performed 
    object_grabber_goal.object_id = ObjectIdCodes::COKE_CAN_UPRIGHT; // specify the object to manipulate                
    object_grabber_goal.object_frame = object_pickup_poseStamped; //and the object's current pose
    object_grabber_goal.grasp_option = object_grabber::object_grabberGoal::DEFAULT_GRASP_STRATEGY; //from above
    object_grabber_goal.speed_factor = 1.0;
    ROS_INFO("sending goal to grab object: ");
    object_grabber_ac.sendGoal(object_grabber_goal, &objectGrabberDoneCb);
    ROS_INFO("waiting on result");
    finished_before_timeout = object_grabber_ac.waitForResult(ros::Duration(30.0));

    if (!finished_before_timeout) {
        ROS_WARN("giving up waiting on result ");
        return 1;
    }
 
    //move to waiting pose
    ROS_INFO("sending command to move to waiting pose");
    object_grabber_goal.action_code = object_grabber::object_grabberGoal::MOVE_TO_WAITING_POSE;
    object_grabber_ac.sendGoal(object_grabber_goal, &objectGrabberDoneCb);
    finished_before_timeout = object_grabber_ac.waitForResult(ros::Duration(30.0));
    if (!finished_before_timeout) {
        ROS_WARN("giving up waiting on result ");
        return 1;
    }
    
    //could instead hand-tune some intermediate, joint-space poses:
    //    Eigen::VectorXd joint_angles;
    // resize to 6 joints and populate w/ magic numbers
    //rtn_val=arm_motion_commander.plan_jspace_path_current_to_qgoal(joint_angles);
    //rtn_val=arm_motion_commander.execute_planned_path(); 
   
    ROS_INFO("sending a dropoff-object command");
    object_grabber_goal.action_code = object_grabber::object_grabberGoal::DROPOFF_OBJECT; //specify the action to be performed 
    object_grabber_goal.object_id = ObjectIdCodes::COKE_CAN_UPRIGHT; // specify the object to manipulate                
    object_grabber_goal.object_frame = object_dropoff_poseStamped; //and the object's current pose
    object_grabber_goal.grasp_option = object_grabber::object_grabberGoal::DEFAULT_GRASP_STRATEGY; //from above
    object_grabber_goal.speed_factor = 1.0;
    ROS_INFO("sending goal to dropoff object: ");
    object_grabber_ac.sendGoal(object_grabber_goal, &objectGrabberDoneCb);
    ROS_INFO("waiting on result");
    finished_before_timeout = object_grabber_ac.waitForResult(ros::Duration(30.0));

    if (!finished_before_timeout) {
        ROS_WARN("giving up waiting on result ");
        return 1;
    }
    return 0;
}
