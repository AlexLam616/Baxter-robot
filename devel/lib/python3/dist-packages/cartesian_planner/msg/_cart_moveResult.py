# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from cartesian_planner/cart_moveResult.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import std_msgs.msg

class cart_moveResult(genpy.Message):
  _md5sum = "72659348ac499e20e188455dede6554a"
  _type = "cartesian_planner/cart_moveResult"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======

# Result Def
# Response codes
uint8 SUCCESS                           = 0

uint8 ARM_RECEIVED_AND_INITIATED_RQST   = 1
uint8 ARM_RECEIVED_AND_COMPLETED_RQST   = 5
uint8 ARM_REQUEST_REJECTED_ALREADY_BUSY = 2

uint8 ARM_SERVER_NOT_BUSY               = 3
uint8 ARM_SERVER_IS_BUSY                = 4

uint8 PATH_IS_VALID                     = 6
uint8 PATH_NOT_VALID                    = 7

uint8 COMMAND_CODE_NOT_RECOGNIZED       = 8
uint8 ARM_STATUS_UNDEFINED              = 9
uint8 NOT_FINISHED_BEFORE_TIMEOUT       = 10

int32       return_code
int32       err_code
string      err_msg
float64     computed_arrival_time
float64[]   q_arm
geometry_msgs/PoseStamped current_pose_gripper
#geometry_msgs/PoseStamped current_pose_flange


================================================================================
MSG: geometry_msgs/PoseStamped
# A Pose with reference coordinate frame and timestamp
Header header
Pose pose

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
  # Pseudo-constants
  SUCCESS = 0
  ARM_RECEIVED_AND_INITIATED_RQST = 1
  ARM_RECEIVED_AND_COMPLETED_RQST = 5
  ARM_REQUEST_REJECTED_ALREADY_BUSY = 2
  ARM_SERVER_NOT_BUSY = 3
  ARM_SERVER_IS_BUSY = 4
  PATH_IS_VALID = 6
  PATH_NOT_VALID = 7
  COMMAND_CODE_NOT_RECOGNIZED = 8
  ARM_STATUS_UNDEFINED = 9
  NOT_FINISHED_BEFORE_TIMEOUT = 10

  __slots__ = ['return_code','err_code','err_msg','computed_arrival_time','q_arm','current_pose_gripper']
  _slot_types = ['int32','int32','string','float64','float64[]','geometry_msgs/PoseStamped']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       return_code,err_code,err_msg,computed_arrival_time,q_arm,current_pose_gripper

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(cart_moveResult, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.return_code is None:
        self.return_code = 0
      if self.err_code is None:
        self.err_code = 0
      if self.err_msg is None:
        self.err_msg = ''
      if self.computed_arrival_time is None:
        self.computed_arrival_time = 0.
      if self.q_arm is None:
        self.q_arm = []
      if self.current_pose_gripper is None:
        self.current_pose_gripper = geometry_msgs.msg.PoseStamped()
    else:
      self.return_code = 0
      self.err_code = 0
      self.err_msg = ''
      self.computed_arrival_time = 0.
      self.q_arm = []
      self.current_pose_gripper = geometry_msgs.msg.PoseStamped()

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
      buff.write(_get_struct_2i().pack(_x.return_code, _x.err_code))
      _x = self.err_msg
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.computed_arrival_time
      buff.write(_get_struct_d().pack(_x))
      length = len(self.q_arm)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.q_arm))
      _x = self
      buff.write(_get_struct_3I().pack(_x.current_pose_gripper.header.seq, _x.current_pose_gripper.header.stamp.secs, _x.current_pose_gripper.header.stamp.nsecs))
      _x = self.current_pose_gripper.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_7d().pack(_x.current_pose_gripper.pose.position.x, _x.current_pose_gripper.pose.position.y, _x.current_pose_gripper.pose.position.z, _x.current_pose_gripper.pose.orientation.x, _x.current_pose_gripper.pose.orientation.y, _x.current_pose_gripper.pose.orientation.z, _x.current_pose_gripper.pose.orientation.w))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.current_pose_gripper is None:
        self.current_pose_gripper = geometry_msgs.msg.PoseStamped()
      end = 0
      _x = self
      start = end
      end += 8
      (_x.return_code, _x.err_code,) = _get_struct_2i().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.err_msg = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.err_msg = str[start:end]
      start = end
      end += 8
      (self.computed_arrival_time,) = _get_struct_d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.q_arm = s.unpack(str[start:end])
      _x = self
      start = end
      end += 12
      (_x.current_pose_gripper.header.seq, _x.current_pose_gripper.header.stamp.secs, _x.current_pose_gripper.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.current_pose_gripper.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.current_pose_gripper.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 56
      (_x.current_pose_gripper.pose.position.x, _x.current_pose_gripper.pose.position.y, _x.current_pose_gripper.pose.position.z, _x.current_pose_gripper.pose.orientation.x, _x.current_pose_gripper.pose.orientation.y, _x.current_pose_gripper.pose.orientation.z, _x.current_pose_gripper.pose.orientation.w,) = _get_struct_7d().unpack(str[start:end])
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
      buff.write(_get_struct_2i().pack(_x.return_code, _x.err_code))
      _x = self.err_msg
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.computed_arrival_time
      buff.write(_get_struct_d().pack(_x))
      length = len(self.q_arm)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.q_arm.tostring())
      _x = self
      buff.write(_get_struct_3I().pack(_x.current_pose_gripper.header.seq, _x.current_pose_gripper.header.stamp.secs, _x.current_pose_gripper.header.stamp.nsecs))
      _x = self.current_pose_gripper.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_7d().pack(_x.current_pose_gripper.pose.position.x, _x.current_pose_gripper.pose.position.y, _x.current_pose_gripper.pose.position.z, _x.current_pose_gripper.pose.orientation.x, _x.current_pose_gripper.pose.orientation.y, _x.current_pose_gripper.pose.orientation.z, _x.current_pose_gripper.pose.orientation.w))
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
      if self.current_pose_gripper is None:
        self.current_pose_gripper = geometry_msgs.msg.PoseStamped()
      end = 0
      _x = self
      start = end
      end += 8
      (_x.return_code, _x.err_code,) = _get_struct_2i().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.err_msg = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.err_msg = str[start:end]
      start = end
      end += 8
      (self.computed_arrival_time,) = _get_struct_d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.q_arm = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      _x = self
      start = end
      end += 12
      (_x.current_pose_gripper.header.seq, _x.current_pose_gripper.header.stamp.secs, _x.current_pose_gripper.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.current_pose_gripper.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.current_pose_gripper.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 56
      (_x.current_pose_gripper.pose.position.x, _x.current_pose_gripper.pose.position.y, _x.current_pose_gripper.pose.position.z, _x.current_pose_gripper.pose.orientation.x, _x.current_pose_gripper.pose.orientation.y, _x.current_pose_gripper.pose.orientation.z, _x.current_pose_gripper.pose.orientation.w,) = _get_struct_7d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2i = None
def _get_struct_2i():
    global _struct_2i
    if _struct_2i is None:
        _struct_2i = struct.Struct("<2i")
    return _struct_2i
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_7d = None
def _get_struct_7d():
    global _struct_7d
    if _struct_7d is None:
        _struct_7d = struct.Struct("<7d")
    return _struct_7d
_struct_d = None
def _get_struct_d():
    global _struct_d
    if _struct_d is None:
        _struct_d = struct.Struct("<d")
    return _struct_d
