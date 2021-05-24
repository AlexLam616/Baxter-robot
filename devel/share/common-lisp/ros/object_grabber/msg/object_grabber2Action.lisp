; Auto-generated. Do not edit!


(cl:in-package object_grabber-msg)


;//! \htmlinclude object_grabber2Action.msg.html

(cl:defclass <object_grabber2Action> (roslisp-msg-protocol:ros-message)
  ((action_goal
    :reader action_goal
    :initarg :action_goal
    :type object_grabber-msg:object_grabber2ActionGoal
    :initform (cl:make-instance 'object_grabber-msg:object_grabber2ActionGoal))
   (action_result
    :reader action_result
    :initarg :action_result
    :type object_grabber-msg:object_grabber2ActionResult
    :initform (cl:make-instance 'object_grabber-msg:object_grabber2ActionResult))
   (action_feedback
    :reader action_feedback
    :initarg :action_feedback
    :type object_grabber-msg:object_grabber2ActionFeedback
    :initform (cl:make-instance 'object_grabber-msg:object_grabber2ActionFeedback)))
)

(cl:defclass object_grabber2Action (<object_grabber2Action>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <object_grabber2Action>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'object_grabber2Action)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name object_grabber-msg:<object_grabber2Action> is deprecated: use object_grabber-msg:object_grabber2Action instead.")))

(cl:ensure-generic-function 'action_goal-val :lambda-list '(m))
(cl:defmethod action_goal-val ((m <object_grabber2Action>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader object_grabber-msg:action_goal-val is deprecated.  Use object_grabber-msg:action_goal instead.")
  (action_goal m))

(cl:ensure-generic-function 'action_result-val :lambda-list '(m))
(cl:defmethod action_result-val ((m <object_grabber2Action>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader object_grabber-msg:action_result-val is deprecated.  Use object_grabber-msg:action_result instead.")
  (action_result m))

(cl:ensure-generic-function 'action_feedback-val :lambda-list '(m))
(cl:defmethod action_feedback-val ((m <object_grabber2Action>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader object_grabber-msg:action_feedback-val is deprecated.  Use object_grabber-msg:action_feedback instead.")
  (action_feedback m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <object_grabber2Action>) ostream)
  "Serializes a message object of type '<object_grabber2Action>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'action_goal) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'action_result) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'action_feedback) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <object_grabber2Action>) istream)
  "Deserializes a message object of type '<object_grabber2Action>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'action_goal) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'action_result) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'action_feedback) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<object_grabber2Action>)))
  "Returns string type for a message object of type '<object_grabber2Action>"
  "object_grabber/object_grabber2Action")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'object_grabber2Action)))
  "Returns string type for a message object of type 'object_grabber2Action"
  "object_grabber/object_grabber2Action")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<object_grabber2Action>)))
  "Returns md5sum for a message object of type '<object_grabber2Action>"
  "020d8c1c2b6e1ffd944819792cf3c1c3")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'object_grabber2Action)))
  "Returns md5sum for a message object of type 'object_grabber2Action"
  "020d8c1c2b6e1ffd944819792cf3c1c3")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<object_grabber2Action>)))
  "Returns full string definition for message of type '<object_grabber2Action>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%object_grabber2ActionGoal action_goal~%object_grabber2ActionResult action_result~%object_grabber2ActionFeedback action_feedback~%~%================================================================================~%MSG: object_grabber/object_grabber2ActionGoal~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%Header header~%actionlib_msgs/GoalID goal_id~%object_grabber2Goal goal~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: actionlib_msgs/GoalID~%# The stamp should store the time at which this goal was requested.~%# It is used by an action server when it tries to preempt all~%# goals that were requested before a certain time~%time stamp~%~%# The id provides a way to associate feedback and~%# result message with specific goal requests. The id~%# specified must be unique.~%string id~%~%~%================================================================================~%MSG: object_grabber/object_grabber2Goal~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%#object_grabber action message~%#pass in an object code and the object's frame (w/rt named frame_id)~%#object_grabber will plan approach, grasp and lift of object~%#returns codes regarding outcome~%~%int32 UPRIGHT_CYLINDER = 1~%int32 GRAB_UPRIGHT_CYLINDER = 1 #synonym~%int32 COKE_CAN = 2~%int32 GRAB_COKE_CAN = 2 #synonym~%int32 GRAB_W_TOOL_Z_APPROACH = 2 #another synonym~%int32 PLACE_UPRIGHT_CYLINDER = 3 #new drop-off command~%int32 PLACE_COKE_CAN = 4 #drop-off coke can~%int32 DROPOFF_ALONG_TOOL_Z = 4 #synonym~%~%int32 MOVE_FLANGE_TO = 5 #specify flange pose to reach~%int32 FINE_MOVE_FLANGE_TO = 6 #precision move to specified flange pose~%int32 MOVE_TO_PRE_POSE = 7 # get hand out of way of camera~%int32 JSPACE_MOVE_FLANGE_TO = 8 # joint-space move to specified flange pose~%~%int32 CLOSE_GRIPPER = 100  #commands to open/close gripper; should specify test value~%int32 OPEN_GRIPPER = 101~%~%#moved these properties to object_manipulation_properties package/library~%#float64 COKE_CAN_APPROACH_DIST = 0.05~%#expect w/ gripper closed on coke can, finger separation should be more than this value:~%#float64 COKE_CAN_GRIPPER_CLOSE_TEST_VAL = 80.0~%~%~%#add more objects here...~%~%~%~%#goal:~%int32 action_code~%int32 object_id~%geometry_msgs/PoseStamped desired_frame  ~%#float64 gripper_test_val~%~%~%================================================================================~%MSG: geometry_msgs/PoseStamped~%# A Pose with reference coordinate frame and timestamp~%Header header~%Pose pose~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%================================================================================~%MSG: object_grabber/object_grabber2ActionResult~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%Header header~%actionlib_msgs/GoalStatus status~%object_grabber2Result result~%~%================================================================================~%MSG: actionlib_msgs/GoalStatus~%GoalID goal_id~%uint8 status~%uint8 PENDING         = 0   # The goal has yet to be processed by the action server~%uint8 ACTIVE          = 1   # The goal is currently being processed by the action server~%uint8 PREEMPTED       = 2   # The goal received a cancel request after it started executing~%                            #   and has since completed its execution (Terminal State)~%uint8 SUCCEEDED       = 3   # The goal was achieved successfully by the action server (Terminal State)~%uint8 ABORTED         = 4   # The goal was aborted during execution by the action server due~%                            #    to some failure (Terminal State)~%uint8 REJECTED        = 5   # The goal was rejected by the action server without being processed,~%                            #    because the goal was unattainable or invalid (Terminal State)~%uint8 PREEMPTING      = 6   # The goal received a cancel request after it started executing~%                            #    and has not yet completed execution~%uint8 RECALLING       = 7   # The goal received a cancel request before it started executing,~%                            #    but the action server has not yet confirmed that the goal is canceled~%uint8 RECALLED        = 8   # The goal received a cancel request before it started executing~%                            #    and was successfully cancelled (Terminal State)~%uint8 LOST            = 9   # An action client can determine that a goal is LOST. This should not be~%                            #    sent over the wire by an action server~%~%#Allow for the user to associate a string with GoalStatus for debugging~%string text~%~%~%================================================================================~%MSG: object_grabber/object_grabber2Result~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%#result definition~%#  response codes...~%int32 SUCCESS=0~%int32 OBJECT_ACQUIRED=0~%int32 FAILED_CANNOT_REACH=1~%int32 FAILED_CANNOT_APPROACH=2~%int32 FAILED_CANNOT_REACH_GRASP_POSE=3~%int32 FAILED_CANNOT_REACH_DEPART_POSE=4~%int32 FAILED_OBJECT_NOT_IN_GRIPPER=5~%int32 FAILED_OBJECT_UNKNOWN=6~%int32 OBJECT_GRABBER_BUSY=7~%int32 OBJECT_GRABBER_CANCELLED=8~%int32 FAILED_CANNOT_REACH_DROPOFF_POSE=9~%int32 FAILED_CANNOT_REACH_DROPOFF_APPROACH=10~%int32 FAILED_CANNOT_REACH_POSE_CARTESIAN_MOVE=11~%int32 FAILED_CANNOT_REACH_JSPACE_MOVE=12~%int32 FAILED_CANNOT_MOVE_CARTESIAN_FINE=13~%int32 FAILED_CANNOT_MOVE_TO_PRE_POSE=14~%int32 ACTION_CODE_UNKNOWN=15~%int32 GRIPPER_IS_OPEN=16~%int32 GRIPPER_IS_CLOSED=17~%int32 GRIPPER_FAILURE=18~%int32 PENDING=19~%int32 OBJECT_DROPPED_OFF = 20~%~%int32 return_code~%geometry_msgs/PoseStamped des_flange_pose_stamped_wrt_torso~%~%================================================================================~%MSG: object_grabber/object_grabber2ActionFeedback~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%Header header~%actionlib_msgs/GoalStatus status~%object_grabber2Feedback feedback~%~%================================================================================~%MSG: object_grabber/object_grabber2Feedback~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%#feedback: optional; ~%int32 fdbk~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'object_grabber2Action)))
  "Returns full string definition for message of type 'object_grabber2Action"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%object_grabber2ActionGoal action_goal~%object_grabber2ActionResult action_result~%object_grabber2ActionFeedback action_feedback~%~%================================================================================~%MSG: object_grabber/object_grabber2ActionGoal~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%Header header~%actionlib_msgs/GoalID goal_id~%object_grabber2Goal goal~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: actionlib_msgs/GoalID~%# The stamp should store the time at which this goal was requested.~%# It is used by an action server when it tries to preempt all~%# goals that were requested before a certain time~%time stamp~%~%# The id provides a way to associate feedback and~%# result message with specific goal requests. The id~%# specified must be unique.~%string id~%~%~%================================================================================~%MSG: object_grabber/object_grabber2Goal~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%#object_grabber action message~%#pass in an object code and the object's frame (w/rt named frame_id)~%#object_grabber will plan approach, grasp and lift of object~%#returns codes regarding outcome~%~%int32 UPRIGHT_CYLINDER = 1~%int32 GRAB_UPRIGHT_CYLINDER = 1 #synonym~%int32 COKE_CAN = 2~%int32 GRAB_COKE_CAN = 2 #synonym~%int32 GRAB_W_TOOL_Z_APPROACH = 2 #another synonym~%int32 PLACE_UPRIGHT_CYLINDER = 3 #new drop-off command~%int32 PLACE_COKE_CAN = 4 #drop-off coke can~%int32 DROPOFF_ALONG_TOOL_Z = 4 #synonym~%~%int32 MOVE_FLANGE_TO = 5 #specify flange pose to reach~%int32 FINE_MOVE_FLANGE_TO = 6 #precision move to specified flange pose~%int32 MOVE_TO_PRE_POSE = 7 # get hand out of way of camera~%int32 JSPACE_MOVE_FLANGE_TO = 8 # joint-space move to specified flange pose~%~%int32 CLOSE_GRIPPER = 100  #commands to open/close gripper; should specify test value~%int32 OPEN_GRIPPER = 101~%~%#moved these properties to object_manipulation_properties package/library~%#float64 COKE_CAN_APPROACH_DIST = 0.05~%#expect w/ gripper closed on coke can, finger separation should be more than this value:~%#float64 COKE_CAN_GRIPPER_CLOSE_TEST_VAL = 80.0~%~%~%#add more objects here...~%~%~%~%#goal:~%int32 action_code~%int32 object_id~%geometry_msgs/PoseStamped desired_frame  ~%#float64 gripper_test_val~%~%~%================================================================================~%MSG: geometry_msgs/PoseStamped~%# A Pose with reference coordinate frame and timestamp~%Header header~%Pose pose~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%================================================================================~%MSG: object_grabber/object_grabber2ActionResult~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%Header header~%actionlib_msgs/GoalStatus status~%object_grabber2Result result~%~%================================================================================~%MSG: actionlib_msgs/GoalStatus~%GoalID goal_id~%uint8 status~%uint8 PENDING         = 0   # The goal has yet to be processed by the action server~%uint8 ACTIVE          = 1   # The goal is currently being processed by the action server~%uint8 PREEMPTED       = 2   # The goal received a cancel request after it started executing~%                            #   and has since completed its execution (Terminal State)~%uint8 SUCCEEDED       = 3   # The goal was achieved successfully by the action server (Terminal State)~%uint8 ABORTED         = 4   # The goal was aborted during execution by the action server due~%                            #    to some failure (Terminal State)~%uint8 REJECTED        = 5   # The goal was rejected by the action server without being processed,~%                            #    because the goal was unattainable or invalid (Terminal State)~%uint8 PREEMPTING      = 6   # The goal received a cancel request after it started executing~%                            #    and has not yet completed execution~%uint8 RECALLING       = 7   # The goal received a cancel request before it started executing,~%                            #    but the action server has not yet confirmed that the goal is canceled~%uint8 RECALLED        = 8   # The goal received a cancel request before it started executing~%                            #    and was successfully cancelled (Terminal State)~%uint8 LOST            = 9   # An action client can determine that a goal is LOST. This should not be~%                            #    sent over the wire by an action server~%~%#Allow for the user to associate a string with GoalStatus for debugging~%string text~%~%~%================================================================================~%MSG: object_grabber/object_grabber2Result~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%#result definition~%#  response codes...~%int32 SUCCESS=0~%int32 OBJECT_ACQUIRED=0~%int32 FAILED_CANNOT_REACH=1~%int32 FAILED_CANNOT_APPROACH=2~%int32 FAILED_CANNOT_REACH_GRASP_POSE=3~%int32 FAILED_CANNOT_REACH_DEPART_POSE=4~%int32 FAILED_OBJECT_NOT_IN_GRIPPER=5~%int32 FAILED_OBJECT_UNKNOWN=6~%int32 OBJECT_GRABBER_BUSY=7~%int32 OBJECT_GRABBER_CANCELLED=8~%int32 FAILED_CANNOT_REACH_DROPOFF_POSE=9~%int32 FAILED_CANNOT_REACH_DROPOFF_APPROACH=10~%int32 FAILED_CANNOT_REACH_POSE_CARTESIAN_MOVE=11~%int32 FAILED_CANNOT_REACH_JSPACE_MOVE=12~%int32 FAILED_CANNOT_MOVE_CARTESIAN_FINE=13~%int32 FAILED_CANNOT_MOVE_TO_PRE_POSE=14~%int32 ACTION_CODE_UNKNOWN=15~%int32 GRIPPER_IS_OPEN=16~%int32 GRIPPER_IS_CLOSED=17~%int32 GRIPPER_FAILURE=18~%int32 PENDING=19~%int32 OBJECT_DROPPED_OFF = 20~%~%int32 return_code~%geometry_msgs/PoseStamped des_flange_pose_stamped_wrt_torso~%~%================================================================================~%MSG: object_grabber/object_grabber2ActionFeedback~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%Header header~%actionlib_msgs/GoalStatus status~%object_grabber2Feedback feedback~%~%================================================================================~%MSG: object_grabber/object_grabber2Feedback~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%#feedback: optional; ~%int32 fdbk~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <object_grabber2Action>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'action_goal))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'action_result))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'action_feedback))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <object_grabber2Action>))
  "Converts a ROS message object to a list"
  (cl:list 'object_grabber2Action
    (cl:cons ':action_goal (action_goal msg))
    (cl:cons ':action_result (action_result msg))
    (cl:cons ':action_feedback (action_feedback msg))
))
