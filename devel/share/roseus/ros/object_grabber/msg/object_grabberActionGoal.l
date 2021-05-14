;; Auto-generated. Do not edit!


(when (boundp 'object_grabber::object_grabberActionGoal)
  (if (not (find-package "OBJECT_GRABBER"))
    (make-package "OBJECT_GRABBER"))
  (shadow 'object_grabberActionGoal (find-package "OBJECT_GRABBER")))
(unless (find-package "OBJECT_GRABBER::OBJECT_GRABBERACTIONGOAL")
  (make-package "OBJECT_GRABBER::OBJECT_GRABBERACTIONGOAL"))

(in-package "ROS")
;;//! \htmlinclude object_grabberActionGoal.msg.html
(if (not (find-package "ACTIONLIB_MSGS"))
  (ros::roseus-add-msgs "actionlib_msgs"))
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass object_grabber::object_grabberActionGoal
  :super ros::object
  :slots (_header _goal_id _goal ))

(defmethod object_grabber::object_grabberActionGoal
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:goal_id __goal_id) (instance actionlib_msgs::GoalID :init))
    ((:goal __goal) (instance object_grabber::object_grabberGoal :init))
    )
   (send-super :init)
   (setq _header __header)
   (setq _goal_id __goal_id)
   (setq _goal __goal)
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:goal_id
   (&rest __goal_id)
   (if (keywordp (car __goal_id))
       (send* _goal_id __goal_id)
     (progn
       (if __goal_id (setq _goal_id (car __goal_id)))
       _goal_id)))
  (:goal
   (&rest __goal)
   (if (keywordp (car __goal))
       (send* _goal __goal)
     (progn
       (if __goal (setq _goal (car __goal)))
       _goal)))
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; actionlib_msgs/GoalID _goal_id
    (send _goal_id :serialization-length)
    ;; object_grabber/object_grabberGoal _goal
    (send _goal :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; actionlib_msgs/GoalID _goal_id
       (send _goal_id :serialize s)
     ;; object_grabber/object_grabberGoal _goal
       (send _goal :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; actionlib_msgs/GoalID _goal_id
     (send _goal_id :deserialize buf ptr-) (incf ptr- (send _goal_id :serialization-length))
   ;; object_grabber/object_grabberGoal _goal
     (send _goal :deserialize buf ptr-) (incf ptr- (send _goal :serialization-length))
   ;;
   self)
  )

(setf (get object_grabber::object_grabberActionGoal :md5sum-) "3ed7e2451ccf211a58f8be3a15ef1aeb")
(setf (get object_grabber::object_grabberActionGoal :datatype-) "object_grabber/object_grabberActionGoal")
(setf (get object_grabber::object_grabberActionGoal :definition-)
      "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======

Header header
actionlib_msgs/GoalID goal_id
object_grabberGoal goal

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

================================================================================
MSG: actionlib_msgs/GoalID
# The stamp should store the time at which this goal was requested.
# It is used by an action server when it tries to preempt all
# goals that were requested before a certain time
time stamp

# The id provides a way to associate feedback and
# result message with specific goal requests. The id
# specified must be unique.
string id


================================================================================
MSG: object_grabber/object_grabberGoal
# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
#object_grabber action message
#pass in an object code and the object's frame (w/rt named frame_id)
#object_grabber will plan approach, grasp and lift of object
#returns codes regarding outcome

# Action Codes

# Pre-Grasp
int32 TEST_CODE                         = 0     # \"ping\" action server
int32 MOVE_TO_WAITING_POSE              = 1     # pre-pose motion: defined on param server out of way of sensors

int32 PLAN_MOVE_TO_GRASP_POSE           = 2     # expects (1) current_object_pose, (2) object_ID, (3) grasp_option, (4) approach_option
                                                # + send separate \"grasp\" command to gripper

int32 PLAN_MOVE_FINE_TO_GRASP_POSE      = 3     # as above, but finer/slower motion 

### Move Object
int32 PLAN_MOVE_OBJECT_JSPACE           = 4     # move grasped object to dest in joint-space
                                                # expects: (i) des_object_pose, (2) object_ID, (3) grasp_option

int32 PLAN_MOVE_OBJECT_CSPACE           = 5     # move grasped object to dest in cart-space
                                                # expects as above

int32 PLAN_MOVE_FINE_OBJECT_CSPACE      = 6     # as above, but finer/slower motion

### Post-Grasp
int32 PLAN_WITHDRAW_FROM_OBJECT         = 7     # after grasp released, use strategy to depart object 
                                                # (1) object_ID, (2) grasp_option, (3) depart_option

int32 PLAN_WITHDRAW_FINE_FROM_OBJECT    = 8     # as above, but finer/slower motion

### Combined actions 
int32 PLAN_OBJECT_GRASP                 = 9     # combine multiple elements above to acquire an object

int32 CART_MOVE_CURRENT_TO_CART_GOAL    = 10    # plan/execute move to cartesian goal specified in \"geometry_msgs/PoseStamped object_frame\"

int32 GRAB_OBJECT                       = 101   # plan/execute object grasp & lift
int32 DROPOFF_OBJECT                    = 102   # plan/execute object placement and arm withdrawal
int32 STRADDLE_OBJECT                   = 103   # plan/execute part of GRAB_OBJECT: move to grasp pose, then halt

int32 SET_SPEED_FACTOR = 10                     # arg: changes trajectory time-scale: > 1.0 ==> slower

### Strategies:
int32 DEFAULT_GRASP_STRATEGY            = 0     # executes approach and depart strategies. 

int32 EXECUTE_PLANNED_MOVE = 100                # accept arm-motion plan and enable its execution

### Gripper commands:
int32 GRIPPER_PREPARE_GRASP_OBJECT      = 20    # Prepare for grasp approach (open fingers)

int32 GRIPPER_GRASP_OBJECT              = 21    # Perform appropriate action to grasp object (assumes gripper in appropriate pose)
                                                # Client does not need to know what type of gripper is used

int32 GRIPPER_RELEASE_OBJECT            = 22    # Release a grasped object
                                                # (1) obj ID, (2) Grasp option

int32 GRIPPER_IS_OBJECT_GRASPED         = 23    # Query (ret bool)
                                                # (1) object_ID, (2) grasp option, and/or (3)  grasp test parameters; 

###                               

#goal:
int32 action_code                               # See codes above (i.e. MOVE_TO_WAITING_POSE, GRAB_OBJECT, DROPOFF_OBJECT)
int32 object_id
int32 grasp_option

# Strategies: approach, grasp, lift, withdraw
int32 approach_strategy
int32 lift_object_strategy
int32 dropoff_strategy
int32 dropoff_withdraw_strategy

geometry_msgs/PoseStamped object_frame          # wrt system_ref_frame or tf to this frame available
float64                   speed_factor          # default 1.0
float64[]                 gripper_test_params


================================================================================
MSG: geometry_msgs/PoseStamped
# A Pose with reference coordinate frame and timestamp
Header header
Pose pose

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of position and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

")



(provide :object_grabber/object_grabberActionGoal "3ed7e2451ccf211a58f8be3a15ef1aeb")

