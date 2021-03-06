;; Auto-generated. Do not edit!


(when (boundp 'object_grabber::object_grabber3ActionGoal)
  (if (not (find-package "OBJECT_GRABBER"))
    (make-package "OBJECT_GRABBER"))
  (shadow 'object_grabber3ActionGoal (find-package "OBJECT_GRABBER")))
(unless (find-package "OBJECT_GRABBER::OBJECT_GRABBER3ACTIONGOAL")
  (make-package "OBJECT_GRABBER::OBJECT_GRABBER3ACTIONGOAL"))

(in-package "ROS")
;;//! \htmlinclude object_grabber3ActionGoal.msg.html
(if (not (find-package "ACTIONLIB_MSGS"))
  (ros::roseus-add-msgs "actionlib_msgs"))
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass object_grabber::object_grabber3ActionGoal
  :super ros::object
  :slots (_header _goal_id _goal ))

(defmethod object_grabber::object_grabber3ActionGoal
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:goal_id __goal_id) (instance actionlib_msgs::GoalID :init))
    ((:goal __goal) (instance object_grabber::object_grabber3Goal :init))
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
    ;; object_grabber/object_grabber3Goal _goal
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
     ;; object_grabber/object_grabber3Goal _goal
       (send _goal :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; actionlib_msgs/GoalID _goal_id
     (send _goal_id :deserialize buf ptr-) (incf ptr- (send _goal_id :serialization-length))
   ;; object_grabber/object_grabber3Goal _goal
     (send _goal :deserialize buf ptr-) (incf ptr- (send _goal :serialization-length))
   ;;
   self)
  )

(setf (get object_grabber::object_grabber3ActionGoal :md5sum-) "f0e78019e4b96145562e653863369f3e")
(setf (get object_grabber::object_grabber3ActionGoal :datatype-) "object_grabber/object_grabber3ActionGoal")
(setf (get object_grabber::object_grabber3ActionGoal :definition-)
      "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======

Header header
actionlib_msgs/GoalID goal_id
object_grabber3Goal goal

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
MSG: object_grabber/object_grabber3Goal
# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
#object_grabber action message
#pass in an object code and the object's frame (w/rt named frame_id)
#object_grabber will plan approach, grasp and lift of object
#returns codes regarding outcome

#action codes:
int32 TEST_CODE = 0   #a simple \"ping\" to action server
int32 MOVE_TO_WAITING_POSE = 1 #move to a pose, defined on param server, that is convenient
                               #e.g., prepared to approach a surface, but out of way of sensors
int32 PLAN_MOVE_TO_GRASP_POSE  =2   #expects parameters of current_object_pose, object_ID, grasp_option, approach_option
                               #must send separate \"grasp\" command to gripper
int32 PLAN_MOVE_FINE_TO_GRASP_POSE  =3   #as above, but finer/slower approach motion
int32 PLAN_MOVE_OBJECT_JSPACE =4    #move a grasped object to a destination pose using simple, joint-space move
                               #expects params: des_object_pose, object_ID, grasp_option (need to know how object is grasped)
int32 PLAN_MOVE_OBJECT_CSPACE = 5   #move a grasped object with Cartesian motion to a desired object pose
                               #params:  des_object_pose, object_ID, grasp_option
int32 PLAN_MOVE_FINE_OBJECT_CSPACE = 6 #as above, but w/ finer, slower motion

int32 PLAN_WITHDRAW_FROM_OBJECT = 7 #with object grasp released, perform departure from object using specified depart strategy
                               #params: object_ID, grasp_option, depart_option
int32 PLAN_WITHDRAW_FINE_FROM_OBJECT = 8 #as above, but slower/more precise motion

int32 PLAN_OBJECT_GRASP = 9  #combine multiple elements above to acquire an object

int32 GRAB_OBJECT = 101 #plan and attempt to execute object acquisition, including grasp and lift
int32 DROPOFF_OBJECT = 102 #plan and attempt to execute object placement and arm withdrawal

int32 SET_SPEED_FACTOR = 10    #use arg speed_factor to change time scale of trajectory plan; larger than 1.0--> slower

#manipulation strategy options:
int32 DEFAULT_GRASP_STRATEGY = 0
#has corresponding default approach and depart strategies

int32 EXECUTE_PLANNED_MOVE = 100 #accept arm-motion plan and enable its execution

#generalized gripper commands:
int32 GRIPPER_PREPARE_GRASP_OBJECT = 20 #may require gripper to prepare for grasp approach, e.g. open fingers
int32 GRIPPER_GRASP_OBJECT = 21        #command to perform appropriate action to grasp object, 
                               #assumes gripper is in appropriate pose, prepared to grasp object
                               #client does not need to know what type of gripper is used
int32 GRIPPER_RELEASE_OBJECT = 22      #command to gripper to release a grasped object
                               #params: object ID and grasp option used; 
int32 GRIPPER_IS_OBJECT_GRASPED = 23   #a query; may require object_ID, grasp option used, and/or corresponding grasp test parameters; 
                               #should return true/false

#goal:
int32 action_code
int32 object_id
int32 grasp_option
int32 approach_strategy
int32 lift_object_strategy
int32 dropoff_strategy
int32 dropoff_withdraw_strategy
geometry_msgs/PoseStamped object_frame  #should be w/rt system_ref_frame, or have tf to this frame available
float64 speed_factor #default to 1.0
float64[] gripper_test_params

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



(provide :object_grabber/object_grabber3ActionGoal "f0e78019e4b96145562e653863369f3e")


