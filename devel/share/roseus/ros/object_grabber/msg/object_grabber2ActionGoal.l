;; Auto-generated. Do not edit!


(when (boundp 'object_grabber::object_grabber2ActionGoal)
  (if (not (find-package "OBJECT_GRABBER"))
    (make-package "OBJECT_GRABBER"))
  (shadow 'object_grabber2ActionGoal (find-package "OBJECT_GRABBER")))
(unless (find-package "OBJECT_GRABBER::OBJECT_GRABBER2ACTIONGOAL")
  (make-package "OBJECT_GRABBER::OBJECT_GRABBER2ACTIONGOAL"))

(in-package "ROS")
;;//! \htmlinclude object_grabber2ActionGoal.msg.html
(if (not (find-package "ACTIONLIB_MSGS"))
  (ros::roseus-add-msgs "actionlib_msgs"))
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass object_grabber::object_grabber2ActionGoal
  :super ros::object
  :slots (_header _goal_id _goal ))

(defmethod object_grabber::object_grabber2ActionGoal
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:goal_id __goal_id) (instance actionlib_msgs::GoalID :init))
    ((:goal __goal) (instance object_grabber::object_grabber2Goal :init))
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
    ;; object_grabber/object_grabber2Goal _goal
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
     ;; object_grabber/object_grabber2Goal _goal
       (send _goal :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; actionlib_msgs/GoalID _goal_id
     (send _goal_id :deserialize buf ptr-) (incf ptr- (send _goal_id :serialization-length))
   ;; object_grabber/object_grabber2Goal _goal
     (send _goal :deserialize buf ptr-) (incf ptr- (send _goal :serialization-length))
   ;;
   self)
  )

(setf (get object_grabber::object_grabber2ActionGoal :md5sum-) "f737f95f4ea69f3126d207ac9db0606b")
(setf (get object_grabber::object_grabber2ActionGoal :datatype-) "object_grabber/object_grabber2ActionGoal")
(setf (get object_grabber::object_grabber2ActionGoal :definition-)
      "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======

Header header
actionlib_msgs/GoalID goal_id
object_grabber2Goal goal

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
MSG: object_grabber/object_grabber2Goal
# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
#object_grabber action message
#pass in an object code and the object's frame (w/rt named frame_id)
#object_grabber will plan approach, grasp and lift of object
#returns codes regarding outcome

int32 UPRIGHT_CYLINDER = 1
int32 GRAB_UPRIGHT_CYLINDER = 1 #synonym
int32 TOY_BLOCK = 2
int32 GRAB_TOY_BLOCK = 2 #synonym
int32 GRAB_W_TOOL_Z_APPROACH = 2 #another synonym
int32 PLACE_UPRIGHT_CYLINDER = 3 #new drop-off command
int32 PLACE_TOY_BLOCK = 4 #drop-off toy block
int32 DROPOFF_ALONG_TOOL_Z = 4 #synonym

int32 MOVE_FLANGE_TO = 5 #specify flange pose to reach
int32 FINE_MOVE_FLANGE_TO = 6 #precision move to specified flange pose
int32 MOVE_TO_PRE_POSE = 7 # get hand out of way of camera
int32 JSPACE_MOVE_FLANGE_TO = 8 # joint-space move to specified flange pose

int32 CLOSE_GRIPPER = 100  #commands to open/close gripper; should specify test value
int32 OPEN_GRIPPER = 101

#moved these properties to object_manipulation_properties package/library
#float64 TOY_BLOCK_APPROACH_DIST = 0.05
#expect w/ gripper closed on toy block, finger separation should be more than this value:
#float64 TOY_BLOCK_GRIPPER_CLOSE_TEST_VAL = 80.0


#add more objects here...



#goal:
int32 action_code
int32 object_id
geometry_msgs/PoseStamped desired_frame  
#float64 gripper_test_val


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



(provide :object_grabber/object_grabber2ActionGoal "f737f95f4ea69f3126d207ac9db0606b")

