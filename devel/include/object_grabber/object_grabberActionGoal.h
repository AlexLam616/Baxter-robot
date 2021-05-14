// Generated by gencpp from file object_grabber/object_grabberActionGoal.msg
// DO NOT EDIT!


#ifndef OBJECT_GRABBER_MESSAGE_OBJECT_GRABBERACTIONGOAL_H
#define OBJECT_GRABBER_MESSAGE_OBJECT_GRABBERACTIONGOAL_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>
#include <actionlib_msgs/GoalID.h>
#include <object_grabber/object_grabberGoal.h>

namespace object_grabber
{
template <class ContainerAllocator>
struct object_grabberActionGoal_
{
  typedef object_grabberActionGoal_<ContainerAllocator> Type;

  object_grabberActionGoal_()
    : header()
    , goal_id()
    , goal()  {
    }
  object_grabberActionGoal_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , goal_id(_alloc)
    , goal(_alloc)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef  ::actionlib_msgs::GoalID_<ContainerAllocator>  _goal_id_type;
  _goal_id_type goal_id;

   typedef  ::object_grabber::object_grabberGoal_<ContainerAllocator>  _goal_type;
  _goal_type goal;





  typedef boost::shared_ptr< ::object_grabber::object_grabberActionGoal_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::object_grabber::object_grabberActionGoal_<ContainerAllocator> const> ConstPtr;

}; // struct object_grabberActionGoal_

typedef ::object_grabber::object_grabberActionGoal_<std::allocator<void> > object_grabberActionGoal;

typedef boost::shared_ptr< ::object_grabber::object_grabberActionGoal > object_grabberActionGoalPtr;
typedef boost::shared_ptr< ::object_grabber::object_grabberActionGoal const> object_grabberActionGoalConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::object_grabber::object_grabberActionGoal_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::object_grabber::object_grabberActionGoal_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::object_grabber::object_grabberActionGoal_<ContainerAllocator1> & lhs, const ::object_grabber::object_grabberActionGoal_<ContainerAllocator2> & rhs)
{
  return lhs.header == rhs.header &&
    lhs.goal_id == rhs.goal_id &&
    lhs.goal == rhs.goal;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::object_grabber::object_grabberActionGoal_<ContainerAllocator1> & lhs, const ::object_grabber::object_grabberActionGoal_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace object_grabber

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::object_grabber::object_grabberActionGoal_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::object_grabber::object_grabberActionGoal_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::object_grabber::object_grabberActionGoal_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::object_grabber::object_grabberActionGoal_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::object_grabber::object_grabberActionGoal_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::object_grabber::object_grabberActionGoal_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::object_grabber::object_grabberActionGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "3ed7e2451ccf211a58f8be3a15ef1aeb";
  }

  static const char* value(const ::object_grabber::object_grabberActionGoal_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x3ed7e2451ccf211aULL;
  static const uint64_t static_value2 = 0x58f8be3a15ef1aebULL;
};

template<class ContainerAllocator>
struct DataType< ::object_grabber::object_grabberActionGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "object_grabber/object_grabberActionGoal";
  }

  static const char* value(const ::object_grabber::object_grabberActionGoal_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::object_grabber::object_grabberActionGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n"
"\n"
"Header header\n"
"actionlib_msgs/GoalID goal_id\n"
"object_grabberGoal goal\n"
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
"MSG: object_grabber/object_grabberGoal\n"
"# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n"
"#object_grabber action message\n"
"#pass in an object code and the object's frame (w/rt named frame_id)\n"
"#object_grabber will plan approach, grasp and lift of object\n"
"#returns codes regarding outcome\n"
"\n"
"# Action Codes\n"
"\n"
"# Pre-Grasp\n"
"int32 TEST_CODE                         = 0     # \"ping\" action server\n"
"int32 MOVE_TO_WAITING_POSE              = 1     # pre-pose motion: defined on param server out of way of sensors\n"
"\n"
"int32 PLAN_MOVE_TO_GRASP_POSE           = 2     # expects (1) current_object_pose, (2) object_ID, (3) grasp_option, (4) approach_option\n"
"                                                # + send separate \"grasp\" command to gripper\n"
"\n"
"int32 PLAN_MOVE_FINE_TO_GRASP_POSE      = 3     # as above, but finer/slower motion \n"
"\n"
"### Move Object\n"
"int32 PLAN_MOVE_OBJECT_JSPACE           = 4     # move grasped object to dest in joint-space\n"
"                                                # expects: (i) des_object_pose, (2) object_ID, (3) grasp_option\n"
"\n"
"int32 PLAN_MOVE_OBJECT_CSPACE           = 5     # move grasped object to dest in cart-space\n"
"                                                # expects as above\n"
"\n"
"int32 PLAN_MOVE_FINE_OBJECT_CSPACE      = 6     # as above, but finer/slower motion\n"
"\n"
"### Post-Grasp\n"
"int32 PLAN_WITHDRAW_FROM_OBJECT         = 7     # after grasp released, use strategy to depart object \n"
"                                                # (1) object_ID, (2) grasp_option, (3) depart_option\n"
"\n"
"int32 PLAN_WITHDRAW_FINE_FROM_OBJECT    = 8     # as above, but finer/slower motion\n"
"\n"
"### Combined actions \n"
"int32 PLAN_OBJECT_GRASP                 = 9     # combine multiple elements above to acquire an object\n"
"\n"
"int32 CART_MOVE_CURRENT_TO_CART_GOAL    = 10    # plan/execute move to cartesian goal specified in \"geometry_msgs/PoseStamped object_frame\"\n"
"\n"
"int32 GRAB_OBJECT                       = 101   # plan/execute object grasp & lift\n"
"int32 DROPOFF_OBJECT                    = 102   # plan/execute object placement and arm withdrawal\n"
"int32 STRADDLE_OBJECT                   = 103   # plan/execute part of GRAB_OBJECT: move to grasp pose, then halt\n"
"\n"
"int32 SET_SPEED_FACTOR = 10                     # arg: changes trajectory time-scale: > 1.0 ==> slower\n"
"\n"
"### Strategies:\n"
"int32 DEFAULT_GRASP_STRATEGY            = 0     # executes approach and depart strategies. \n"
"\n"
"int32 EXECUTE_PLANNED_MOVE = 100                # accept arm-motion plan and enable its execution\n"
"\n"
"### Gripper commands:\n"
"int32 GRIPPER_PREPARE_GRASP_OBJECT      = 20    # Prepare for grasp approach (open fingers)\n"
"\n"
"int32 GRIPPER_GRASP_OBJECT              = 21    # Perform appropriate action to grasp object (assumes gripper in appropriate pose)\n"
"                                                # Client does not need to know what type of gripper is used\n"
"\n"
"int32 GRIPPER_RELEASE_OBJECT            = 22    # Release a grasped object\n"
"                                                # (1) obj ID, (2) Grasp option\n"
"\n"
"int32 GRIPPER_IS_OBJECT_GRASPED         = 23    # Query (ret bool)\n"
"                                                # (1) object_ID, (2) grasp option, and/or (3)  grasp test parameters; \n"
"\n"
"###                               \n"
"\n"
"#goal:\n"
"int32 action_code                               # See codes above (i.e. MOVE_TO_WAITING_POSE, GRAB_OBJECT, DROPOFF_OBJECT)\n"
"int32 object_id\n"
"int32 grasp_option\n"
"\n"
"# Strategies: approach, grasp, lift, withdraw\n"
"int32 approach_strategy\n"
"int32 lift_object_strategy\n"
"int32 dropoff_strategy\n"
"int32 dropoff_withdraw_strategy\n"
"\n"
"geometry_msgs/PoseStamped object_frame          # wrt system_ref_frame or tf to this frame available\n"
"float64                   speed_factor          # default 1.0\n"
"float64[]                 gripper_test_params\n"
"\n"
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
;
  }

  static const char* value(const ::object_grabber::object_grabberActionGoal_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::object_grabber::object_grabberActionGoal_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.goal_id);
      stream.next(m.goal);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct object_grabberActionGoal_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::object_grabber::object_grabberActionGoal_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::object_grabber::object_grabberActionGoal_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "goal_id: ";
    s << std::endl;
    Printer< ::actionlib_msgs::GoalID_<ContainerAllocator> >::stream(s, indent + "  ", v.goal_id);
    s << indent << "goal: ";
    s << std::endl;
    Printer< ::object_grabber::object_grabberGoal_<ContainerAllocator> >::stream(s, indent + "  ", v.goal);
  }
};

} // namespace message_operations
} // namespace ros

#endif // OBJECT_GRABBER_MESSAGE_OBJECT_GRABBERACTIONGOAL_H
