# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from part_fetcher/PartFetcherGoal.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import std_msgs.msg

class PartFetcherGoal(genpy.Message):
  _md5sum = "3ed50a2a1765af4bdef88bc97e5adc74"
  _type = "part_fetcher/PartFetcherGoal"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
#action message for part fetcher
#specify a part ID, starting pose, and desired destination pose
int32 object_id
geometry_msgs/PoseStamped object_frame
geometry_msgs/PoseStamped desired_frame

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
  __slots__ = ['object_id','object_frame','desired_frame']
  _slot_types = ['int32','geometry_msgs/PoseStamped','geometry_msgs/PoseStamped']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       object_id,object_frame,desired_frame

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(PartFetcherGoal, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.object_id is None:
        self.object_id = 0
      if self.object_frame is None:
        self.object_frame = geometry_msgs.msg.PoseStamped()
      if self.desired_frame is None:
        self.desired_frame = geometry_msgs.msg.PoseStamped()
    else:
      self.object_id = 0
      self.object_frame = geometry_msgs.msg.PoseStamped()
      self.desired_frame = geometry_msgs.msg.PoseStamped()

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
      buff.write(_get_struct_i3I().pack(_x.object_id, _x.object_frame.header.seq, _x.object_frame.header.stamp.secs, _x.object_frame.header.stamp.nsecs))
      _x = self.object_frame.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_7d3I().pack(_x.object_frame.pose.position.x, _x.object_frame.pose.position.y, _x.object_frame.pose.position.z, _x.object_frame.pose.orientation.x, _x.object_frame.pose.orientation.y, _x.object_frame.pose.orientation.z, _x.object_frame.pose.orientation.w, _x.desired_frame.header.seq, _x.desired_frame.header.stamp.secs, _x.desired_frame.header.stamp.nsecs))
      _x = self.desired_frame.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_7d().pack(_x.desired_frame.pose.position.x, _x.desired_frame.pose.position.y, _x.desired_frame.pose.position.z, _x.desired_frame.pose.orientation.x, _x.desired_frame.pose.orientation.y, _x.desired_frame.pose.orientation.z, _x.desired_frame.pose.orientation.w))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.object_frame is None:
        self.object_frame = geometry_msgs.msg.PoseStamped()
      if self.desired_frame is None:
        self.desired_frame = geometry_msgs.msg.PoseStamped()
      end = 0
      _x = self
      start = end
      end += 16
      (_x.object_id, _x.object_frame.header.seq, _x.object_frame.header.stamp.secs, _x.object_frame.header.stamp.nsecs,) = _get_struct_i3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.object_frame.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.object_frame.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 68
      (_x.object_frame.pose.position.x, _x.object_frame.pose.position.y, _x.object_frame.pose.position.z, _x.object_frame.pose.orientation.x, _x.object_frame.pose.orientation.y, _x.object_frame.pose.orientation.z, _x.object_frame.pose.orientation.w, _x.desired_frame.header.seq, _x.desired_frame.header.stamp.secs, _x.desired_frame.header.stamp.nsecs,) = _get_struct_7d3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.desired_frame.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.desired_frame.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 56
      (_x.desired_frame.pose.position.x, _x.desired_frame.pose.position.y, _x.desired_frame.pose.position.z, _x.desired_frame.pose.orientation.x, _x.desired_frame.pose.orientation.y, _x.desired_frame.pose.orientation.z, _x.desired_frame.pose.orientation.w,) = _get_struct_7d().unpack(str[start:end])
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
      buff.write(_get_struct_i3I().pack(_x.object_id, _x.object_frame.header.seq, _x.object_frame.header.stamp.secs, _x.object_frame.header.stamp.nsecs))
      _x = self.object_frame.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_7d3I().pack(_x.object_frame.pose.position.x, _x.object_frame.pose.position.y, _x.object_frame.pose.position.z, _x.object_frame.pose.orientation.x, _x.object_frame.pose.orientation.y, _x.object_frame.pose.orientation.z, _x.object_frame.pose.orientation.w, _x.desired_frame.header.seq, _x.desired_frame.header.stamp.secs, _x.desired_frame.header.stamp.nsecs))
      _x = self.desired_frame.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_7d().pack(_x.desired_frame.pose.position.x, _x.desired_frame.pose.position.y, _x.desired_frame.pose.position.z, _x.desired_frame.pose.orientation.x, _x.desired_frame.pose.orientation.y, _x.desired_frame.pose.orientation.z, _x.desired_frame.pose.orientation.w))
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
      if self.object_frame is None:
        self.object_frame = geometry_msgs.msg.PoseStamped()
      if self.desired_frame is None:
        self.desired_frame = geometry_msgs.msg.PoseStamped()
      end = 0
      _x = self
      start = end
      end += 16
      (_x.object_id, _x.object_frame.header.seq, _x.object_frame.header.stamp.secs, _x.object_frame.header.stamp.nsecs,) = _get_struct_i3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.object_frame.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.object_frame.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 68
      (_x.object_frame.pose.position.x, _x.object_frame.pose.position.y, _x.object_frame.pose.position.z, _x.object_frame.pose.orientation.x, _x.object_frame.pose.orientation.y, _x.object_frame.pose.orientation.z, _x.object_frame.pose.orientation.w, _x.desired_frame.header.seq, _x.desired_frame.header.stamp.secs, _x.desired_frame.header.stamp.nsecs,) = _get_struct_7d3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.desired_frame.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.desired_frame.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 56
      (_x.desired_frame.pose.position.x, _x.desired_frame.pose.position.y, _x.desired_frame.pose.position.z, _x.desired_frame.pose.orientation.x, _x.desired_frame.pose.orientation.y, _x.desired_frame.pose.orientation.z, _x.desired_frame.pose.orientation.w,) = _get_struct_7d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_7d = None
def _get_struct_7d():
    global _struct_7d
    if _struct_7d is None:
        _struct_7d = struct.Struct("<7d")
    return _struct_7d
_struct_7d3I = None
def _get_struct_7d3I():
    global _struct_7d3I
    if _struct_7d3I is None:
        _struct_7d3I = struct.Struct("<7d3I")
    return _struct_7d3I
_struct_i3I = None
def _get_struct_i3I():
    global _struct_i3I
    if _struct_i3I is None:
        _struct_i3I = struct.Struct("<i3I")
    return _struct_i3I
