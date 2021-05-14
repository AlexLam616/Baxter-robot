# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from object_grabber/object_grabberActionGoal.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import actionlib_msgs.msg
import genpy
import geometry_msgs.msg
import object_grabber.msg
import std_msgs.msg

class object_grabberActionGoal(genpy.Message):
  _md5sum = "3ed7e2451ccf211a58f8be3a15ef1aeb"
  _type = "object_grabber/object_grabberActionGoal"
  _has_header = True  # flag to mark the presence of a Header object
  _full_text = """# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======

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
int32 TEST_CODE                         = 0     # "ping" action server
int32 MOVE_TO_WAITING_POSE              = 1     # pre-pose motion: defined on param server out of way of sensors

int32 PLAN_MOVE_TO_GRASP_POSE           = 2     # expects (1) current_object_pose, (2) object_ID, (3) grasp_option, (4) approach_option
                                                # + send separate "grasp" command to gripper

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

int32 CART_MOVE_CURRENT_TO_CART_GOAL    = 10    # plan/execute move to cartesian goal specified in "geometry_msgs/PoseStamped object_frame"

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
"""
  __slots__ = ['header','goal_id','goal']
  _slot_types = ['std_msgs/Header','actionlib_msgs/GoalID','object_grabber/object_grabberGoal']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,goal_id,goal

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(object_grabberActionGoal, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.goal_id is None:
        self.goal_id = actionlib_msgs.msg.GoalID()
      if self.goal is None:
        self.goal = object_grabber.msg.object_grabberGoal()
    else:
      self.header = std_msgs.msg.Header()
      self.goal_id = actionlib_msgs.msg.GoalID()
      self.goal = object_grabber.msg.object_grabberGoal()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2I().pack(_x.goal_id.stamp.secs, _x.goal_id.stamp.nsecs))
      _x = self.goal_id.id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_7i3I().pack(_x.goal.action_code, _x.goal.object_id, _x.goal.grasp_option, _x.goal.approach_strategy, _x.goal.lift_object_strategy, _x.goal.dropoff_strategy, _x.goal.dropoff_withdraw_strategy, _x.goal.object_frame.header.seq, _x.goal.object_frame.header.stamp.secs, _x.goal.object_frame.header.stamp.nsecs))
      _x = self.goal.object_frame.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_8d().pack(_x.goal.object_frame.pose.position.x, _x.goal.object_frame.pose.position.y, _x.goal.object_frame.pose.position.z, _x.goal.object_frame.pose.orientation.x, _x.goal.object_frame.pose.orientation.y, _x.goal.object_frame.pose.orientation.z, _x.goal.object_frame.pose.orientation.w, _x.goal.speed_factor))
      length = len(self.goal.gripper_test_params)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.goal.gripper_test_params))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.goal_id is None:
        self.goal_id = actionlib_msgs.msg.GoalID()
      if self.goal is None:
        self.goal = object_grabber.msg.object_grabberGoal()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.goal_id.stamp.secs, _x.goal_id.stamp.nsecs,) = _get_struct_2I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.goal_id.id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.goal_id.id = str[start:end]
      _x = self
      start = end
      end += 40
      (_x.goal.action_code, _x.goal.object_id, _x.goal.grasp_option, _x.goal.approach_strategy, _x.goal.lift_object_strategy, _x.goal.dropoff_strategy, _x.goal.dropoff_withdraw_strategy, _x.goal.object_frame.header.seq, _x.goal.object_frame.header.stamp.secs, _x.goal.object_frame.header.stamp.nsecs,) = _get_struct_7i3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.goal.object_frame.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.goal.object_frame.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 64
      (_x.goal.object_frame.pose.position.x, _x.goal.object_frame.pose.position.y, _x.goal.object_frame.pose.position.z, _x.goal.object_frame.pose.orientation.x, _x.goal.object_frame.pose.orientation.y, _x.goal.object_frame.pose.orientation.z, _x.goal.object_frame.pose.orientation.w, _x.goal.speed_factor,) = _get_struct_8d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.goal.gripper_test_params = s.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2I().pack(_x.goal_id.stamp.secs, _x.goal_id.stamp.nsecs))
      _x = self.goal_id.id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_7i3I().pack(_x.goal.action_code, _x.goal.object_id, _x.goal.grasp_option, _x.goal.approach_strategy, _x.goal.lift_object_strategy, _x.goal.dropoff_strategy, _x.goal.dropoff_withdraw_strategy, _x.goal.object_frame.header.seq, _x.goal.object_frame.header.stamp.secs, _x.goal.object_frame.header.stamp.nsecs))
      _x = self.goal.object_frame.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_8d().pack(_x.goal.object_frame.pose.position.x, _x.goal.object_frame.pose.position.y, _x.goal.object_frame.pose.position.z, _x.goal.object_frame.pose.orientation.x, _x.goal.object_frame.pose.orientation.y, _x.goal.object_frame.pose.orientation.z, _x.goal.object_frame.pose.orientation.w, _x.goal.speed_factor))
      length = len(self.goal.gripper_test_params)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.goal.gripper_test_params.tostring())
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.goal_id is None:
        self.goal_id = actionlib_msgs.msg.GoalID()
      if self.goal is None:
        self.goal = object_grabber.msg.object_grabberGoal()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.goal_id.stamp.secs, _x.goal_id.stamp.nsecs,) = _get_struct_2I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.goal_id.id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.goal_id.id = str[start:end]
      _x = self
      start = end
      end += 40
      (_x.goal.action_code, _x.goal.object_id, _x.goal.grasp_option, _x.goal.approach_strategy, _x.goal.lift_object_strategy, _x.goal.dropoff_strategy, _x.goal.dropoff_withdraw_strategy, _x.goal.object_frame.header.seq, _x.goal.object_frame.header.stamp.secs, _x.goal.object_frame.header.stamp.nsecs,) = _get_struct_7i3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.goal.object_frame.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.goal.object_frame.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 64
      (_x.goal.object_frame.pose.position.x, _x.goal.object_frame.pose.position.y, _x.goal.object_frame.pose.position.z, _x.goal.object_frame.pose.orientation.x, _x.goal.object_frame.pose.orientation.y, _x.goal.object_frame.pose.orientation.z, _x.goal.object_frame.pose.orientation.w, _x.goal.speed_factor,) = _get_struct_8d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.goal.gripper_test_params = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2I = None
def _get_struct_2I():
    global _struct_2I
    if _struct_2I is None:
        _struct_2I = struct.Struct("<2I")
    return _struct_2I
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_7i3I = None
def _get_struct_7i3I():
    global _struct_7i3I
    if _struct_7i3I is None:
        _struct_7i3I = struct.Struct("<7i3I")
    return _struct_7i3I
_struct_8d = None
def _get_struct_8d():
    global _struct_8d
    if _struct_8d is None:
        _struct_8d = struct.Struct("<8d")
    return _struct_8d