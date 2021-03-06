// Generated by gencpp from file coordinator/ManipTaskAction.msg
// DO NOT EDIT!


#ifndef COORDINATOR_MESSAGE_MANIPTASKACTION_H
#define COORDINATOR_MESSAGE_MANIPTASKACTION_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <coordinator/ManipTaskActionGoal.h>
#include <coordinator/ManipTaskActionResult.h>
#include <coordinator/ManipTaskActionFeedback.h>

namespace coordinator
{
template <class ContainerAllocator>
struct ManipTaskAction_
{
  typedef ManipTaskAction_<ContainerAllocator> Type;

  ManipTaskAction_()
    : action_goal()
    , action_result()
    , action_feedback()  {
    }
  ManipTaskAction_(const ContainerAllocator& _alloc)
    : action_goal(_alloc)
    , action_result(_alloc)
    , action_feedback(_alloc)  {
  (void)_alloc;
    }



   typedef  ::coordinator::ManipTaskActionGoal_<ContainerAllocator>  _action_goal_type;
  _action_goal_type action_goal;

   typedef  ::coordinator::ManipTaskActionResult_<ContainerAllocator>  _action_result_type;
  _action_result_type action_result;

   typedef  ::coordinator::ManipTaskActionFeedback_<ContainerAllocator>  _action_feedback_type;
  _action_feedback_type action_feedback;





  typedef boost::shared_ptr< ::coordinator::ManipTaskAction_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::coordinator::ManipTaskAction_<ContainerAllocator> const> ConstPtr;

}; // struct ManipTaskAction_

typedef ::coordinator::ManipTaskAction_<std::allocator<void> > ManipTaskAction;

typedef boost::shared_ptr< ::coordinator::ManipTaskAction > ManipTaskActionPtr;
typedef boost::shared_ptr< ::coordinator::ManipTaskAction const> ManipTaskActionConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::coordinator::ManipTaskAction_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::coordinator::ManipTaskAction_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::coordinator::ManipTaskAction_<ContainerAllocator1> & lhs, const ::coordinator::ManipTaskAction_<ContainerAllocator2> & rhs)
{
  return lhs.action_goal == rhs.action_goal &&
    lhs.action_result == rhs.action_result &&
    lhs.action_feedback == rhs.action_feedback;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::coordinator::ManipTaskAction_<ContainerAllocator1> & lhs, const ::coordinator::ManipTaskAction_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace coordinator

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::coordinator::ManipTaskAction_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::coordinator::ManipTaskAction_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::coordinator::ManipTaskAction_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::coordinator::ManipTaskAction_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::coordinator::ManipTaskAction_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::coordinator::ManipTaskAction_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::coordinator::ManipTaskAction_<ContainerAllocator> >
{
  static const char* value()
  {
    return "b0d72a10459cfe87a5243cfd55aca4ab";
  }

  static const char* value(const ::coordinator::ManipTaskAction_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xb0d72a10459cfe87ULL;
  static const uint64_t static_value2 = 0xa5243cfd55aca4abULL;
};

template<class ContainerAllocator>
struct DataType< ::coordinator::ManipTaskAction_<ContainerAllocator> >
{
  static const char* value()
  {
    return "coordinator/ManipTaskAction";
  }

  static const char* value(const ::coordinator::ManipTaskAction_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::coordinator::ManipTaskAction_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n"
"\n"
"ManipTaskActionGoal action_goal\n"
"ManipTaskActionResult action_result\n"
"ManipTaskActionFeedback action_feedback\n"
"\n"
"================================================================================\n"
"MSG: coordinator/ManipTaskActionGoal\n"
"# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n"
"\n"
"Header header\n"
"actionlib_msgs/GoalID goal_id\n"
"ManipTaskGoal goal\n"
"\n"
"================================================================================\n"
"MSG: std_msgs/Header\n"
"# Standard metadata for higher-level stamped data types.\n"
"# This is generally used to communicate timestamped data \n"
"# in a particular coordinate frame.\n"
"# \n"
"# sequence ID: consecutively increasing ID \n"
"uint32 seq\n"
"#Two-integer timestamp that is expressed as:\n"
"# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n"
"# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n"
"# time-handling sugar is provided by the client library\n"
"time stamp\n"
"#Frame this data is associated with\n"
"string frame_id\n"
"\n"
"================================================================================\n"
"MSG: actionlib_msgs/GoalID\n"
"# The stamp should store the time at which this goal was requested.\n"
"# It is used by an action server when it tries to preempt all\n"
"# goals that were requested before a certain time\n"
"time stamp\n"
"\n"
"# The id provides a way to associate feedback and\n"
"# result message with specific goal requests. The id\n"
"# specified must be unique.\n"
"string id\n"
"\n"
"\n"
"================================================================================\n"
"MSG: coordinator/ManipTaskGoal\n"
"# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n"
"#goal: specify object code, perception type (incl blind), dropoff location, optional pickup location\n"
"#task codes:\n"
"int32 PCL_VISION = 1 # could have more camera sources to refer to\n"
"int32 BLIND_MANIP = 2 #expect pose specified in pickup_location field\n"
"\n"
"#action codes:\n"
"int32 GET_PICKUP_POSE = 1 #low level ops; maybe don't implement\n"
"int32 WAIT_FOR_FINDER = 101\n"
"\n"
"int32 FIND_TABLE_SURFACE = 2 #do this once, and re-use result for multiple objects\n"
"int32 WAIT_FIND_TABLE_SURFACE = 102\n"
"\n"
"int32 GRAB_OBJECT = 3 #assumes use of current pickup pose,\n"
"                      #whether provided for \"blind\" manip, or found\n"
"                      #from use of PCL_VISION\n"
"int32 WAIT_FOR_GRAB_OBJECT = 103    \n"
"                 \n"
"int32 DROPOFF_OBJECT = 4 #must provide dropoff_frame in goal msg\n"
"int32 WAIT_FOR_DROPOFF_OBJECT = 104\n"
"\n"
"#int32 MANIP_OBJECT = 5 #macro: does perception, grab, and dropoff\n"
"                       #MUST provide dropoff frame, and means to\n"
"                       #get pickup_frame\n"
"\n"
"int32 STRADDLE_OBJECT = 8 #test mode--simply straddle object, but don't grasp it\n"
"int32 WAIT_FOR_STRADDLE_OBJECT = 108\n"
"\n"
"int32 CART_MOVE_TO_GRIPPER_POSE = 9\n"
"int32 WAIT_FOR_CART_MOVE = 109\n"
"                       \n"
"int32 NO_CURRENT_TASK = 6\n"
"int32 MOVE_TO_PRE_POSE = 7\n"
"int32 WAIT_FOR_MOVE_TO_PREPOSE = 107\n"
"int32 WAIT_FOR_MOVE = 107 #generic wait-for-move status\n"
"\n"
"int32 ABORT= 666\n"
"\n"
"#goal specification:\n"
"int32 action_code #what action should be performed?\n"
"int32 object_code #refer to a-priori known object types by object-ID codes\n"
"geometry_msgs/PoseStamped pickup_frame #specify object coords for pickup \n"
"geometry_msgs/PoseStamped dropoff_frame #specify desired drop-off coords of object's frame\n"
"geometry_msgs/PoseStamped gripper_goal_frame #a goal frame to move gripper\n"
"int32 perception_source  #e.g. name a camera source\n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/PoseStamped\n"
"# A Pose with reference coordinate frame and timestamp\n"
"Header header\n"
"Pose pose\n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/Pose\n"
"# A representation of pose in free space, composed of position and orientation. \n"
"Point position\n"
"Quaternion orientation\n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/Point\n"
"# This contains the position of a point in free space\n"
"float64 x\n"
"float64 y\n"
"float64 z\n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/Quaternion\n"
"# This represents an orientation in free space in quaternion form.\n"
"\n"
"float64 x\n"
"float64 y\n"
"float64 z\n"
"float64 w\n"
"\n"
"================================================================================\n"
"MSG: coordinator/ManipTaskActionResult\n"
"# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n"
"\n"
"Header header\n"
"actionlib_msgs/GoalStatus status\n"
"ManipTaskResult result\n"
"\n"
"================================================================================\n"
"MSG: actionlib_msgs/GoalStatus\n"
"GoalID goal_id\n"
"uint8 status\n"
"uint8 PENDING         = 0   # The goal has yet to be processed by the action server\n"
"uint8 ACTIVE          = 1   # The goal is currently being processed by the action server\n"
"uint8 PREEMPTED       = 2   # The goal received a cancel request after it started executing\n"
"                            #   and has since completed its execution (Terminal State)\n"
"uint8 SUCCEEDED       = 3   # The goal was achieved successfully by the action server (Terminal State)\n"
"uint8 ABORTED         = 4   # The goal was aborted during execution by the action server due\n"
"                            #    to some failure (Terminal State)\n"
"uint8 REJECTED        = 5   # The goal was rejected by the action server without being processed,\n"
"                            #    because the goal was unattainable or invalid (Terminal State)\n"
"uint8 PREEMPTING      = 6   # The goal received a cancel request after it started executing\n"
"                            #    and has not yet completed execution\n"
"uint8 RECALLING       = 7   # The goal received a cancel request before it started executing,\n"
"                            #    but the action server has not yet confirmed that the goal is canceled\n"
"uint8 RECALLED        = 8   # The goal received a cancel request before it started executing\n"
"                            #    and was successfully cancelled (Terminal State)\n"
"uint8 LOST            = 9   # An action client can determine that a goal is LOST. This should not be\n"
"                            #    sent over the wire by an action server\n"
"\n"
"#Allow for the user to associate a string with GoalStatus for debugging\n"
"string text\n"
"\n"
"\n"
"================================================================================\n"
"MSG: coordinator/ManipTaskResult\n"
"# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n"
"#return codes:\n"
"int32 MANIP_SUCCESS = 0\n"
"int32 FAILED_PERCEPTION = 1\n"
"int32 FAILED_PICKUP_PLAN =2 \n"
"int32 FAILED_DROPOFF_PLAN=3\n"
"int32 FAILED_PICKUP=4\n"
"int32 FAILED_DROPOFF=5\n"
"int32 DROPPED_OBJECT = 6\n"
"int32 ABORTED = 7\n"
"int32 PENDING = 8\n"
"int32 FAILED_MOVE = 9\n"
"\n"
"int32 manip_return_code\n"
"int32 object_grabber_return_code\n"
"geometry_msgs/PoseStamped des_gripper_pose\n"
"int32 object_finder_return_code\n"
"geometry_msgs/PoseStamped object_pose\n"
"\n"
"\n"
"================================================================================\n"
"MSG: coordinator/ManipTaskActionFeedback\n"
"# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n"
"\n"
"Header header\n"
"actionlib_msgs/GoalStatus status\n"
"ManipTaskFeedback feedback\n"
"\n"
"================================================================================\n"
"MSG: coordinator/ManipTaskFeedback\n"
"# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n"
"#feedback codes:  perception_busy; planning_busy; pickup_busy; dropoff_busy\n"
"int32 RECEIVED_NEW_TASK = 0\n"
"int32 PERCEPTION_BUSY = 1\n"
"int32 PICKUP_PLANNING_BUSY = 2\n"
"int32 PICKUP_MOTION_BUSY = 3\n"
"int32 PICKUP_SUCCESSFUL = 103\n"
"int32 DROPOFF_PLANNING_BUSY = 4\n"
"int32 DROPOFF_MOTION_BUSY = 5\n"
"int32 NO_CURRENT_TASK = 6\n"
"int32 ABORTED = 7\n"
"int32 COMPLETED_MOVE = 8\n"
"int32 COMPLETED_DROPOFF = 9\n"
"int32 PREPOSE_MOVE_BUSY = 10\n"
"int32 MOVE_BUSY = 11\n"
"\n"
"\n"
"int32 feedback_status\n"
"\n"
;
  }

  static const char* value(const ::coordinator::ManipTaskAction_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::coordinator::ManipTaskAction_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.action_goal);
      stream.next(m.action_result);
      stream.next(m.action_feedback);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct ManipTaskAction_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::coordinator::ManipTaskAction_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::coordinator::ManipTaskAction_<ContainerAllocator>& v)
  {
    s << indent << "action_goal: ";
    s << std::endl;
    Printer< ::coordinator::ManipTaskActionGoal_<ContainerAllocator> >::stream(s, indent + "  ", v.action_goal);
    s << indent << "action_result: ";
    s << std::endl;
    Printer< ::coordinator::ManipTaskActionResult_<ContainerAllocator> >::stream(s, indent + "  ", v.action_result);
    s << indent << "action_feedback: ";
    s << std::endl;
    Printer< ::coordinator::ManipTaskActionFeedback_<ContainerAllocator> >::stream(s, indent + "  ", v.action_feedback);
  }
};

} // namespace message_operations
} // namespace ros

#endif // COORDINATOR_MESSAGE_MANIPTASKACTION_H
