# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from arm_motion_action/arm_interfaceGoal.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import std_msgs.msg

class arm_interfaceGoal(genpy.Message):
  _md5sum = "36fc51b5a2a5b9b94726c66530e4f485"
  _type = "arm_motion_action/arm_interfaceGoal"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
#cartesian-move action interface
#minimally, it may contain just a command code
#more generally, it may contain desired tool-frame pose, as well
# as gripper pose (gripper opening, or vacuum gripper on/off)
# and an arrival time for the move
# It is assumed that a move starts from the previous commanded pose, or from the current joint state

#return codes provide status info, e.g. if a proposed move is reachable

#define message constants:  
uint8 ARM_TEST_MODE = 0

#queries
uint8 ARM_IS_SERVER_BUSY_QUERY = 1
uint8 ARM_QUERY_IS_PATH_VALID = 2
uint8 GET_TOOL_POSE = 5
uint8 GET_Q_DATA = 7

#requests for motion plans; 
uint8 PLAN_JSPACE_TRAJ_CURRENT_TO_WAITING_POSE=20
uint8 PLAN_JSPACE_TRAJ_CURRENT_TO_QGOAL = 21
uint8 PLAN_JSPACE_TRAJ_CURRENT_TO_CART_TOOL_POSE = 22 #plan a joint-space path from current arm pose to some IK soln of Cartesian goal

uint8 PLAN_CARTESIAN_TRAJ_CURRENT_TO_DES_TOOL_POSE = 23
uint8 PLAN_CARTESIAN_TRAJ_QSTART_TO_DES_TOOL_POSE = 24
uint8 PLAN_CARTESIAN_TRAJ_QPREV_TO_DES_TOOL_POSE = 25

uint8 CLEAR_MULTI_TRAJ_PLAN = 26
uint8 APPEND_MULTI_TRAJ_CART_SEGMENT = 27
uint8 APPEND_MULTI_TRAJ_JSPACE_SEGMENT = 28
uint8 TEST_PATH_FOR_DISCONTINUITIES = 29
uint8 GET_NUM_PATH_SEGMENTS = 30
uint8 GET_REPLANNED_ARRIVAL_TIMES = 31
uint8 REPLAN_DISCONTINUITIES = 32

uint8 REFINE_PLANNED_TRAJECTORY = 41 #if used approx IK soln, use this option to refine solns
uint8 SEGMENT_DISCONTINUOUS_TRAJ = 42 #if soln is discontinuous, segment it into a multi-traj plan
# return the number of new segments and their respective arrival times

# request to preview plan:
#uint8 DISPLAY_TRAJECTORY = 50

#MOVE command!
uint8 EXECUTE_PLANNED_TRAJ = 100
#specify a segment number to be executed from a multi-segment trajectory
uint8 EXECUTE_TRAJ_NSEG = 101
#for a path with discontinuities, command arm to go to first pose of segment nseg
#specify the path segment in element "nseg"
uint8 GOTO_NSEG_START = 102

#uint8 ARM_DESCEND_20CM=101
#uint8 ARM_DEPART_20CM=102


#goal:
int32 command_code
geometry_msgs/PoseStamped des_pose_gripper
float64[] arm_dp #to command a 3-D vector displacement relative to current pose, fixed orientation
float64[] q_goal
float64[] q_start
int32 nsteps
float64 arrival_time
int32 nseg #to choose one of NSEG segments in a multi-traj vector
#float64 time_scale_stretch_factor

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
  ARM_TEST_MODE = 0
  ARM_IS_SERVER_BUSY_QUERY = 1
  ARM_QUERY_IS_PATH_VALID = 2
  GET_TOOL_POSE = 5
  GET_Q_DATA = 7
  PLAN_JSPACE_TRAJ_CURRENT_TO_WAITING_POSE = 20
  PLAN_JSPACE_TRAJ_CURRENT_TO_QGOAL = 21
  PLAN_JSPACE_TRAJ_CURRENT_TO_CART_TOOL_POSE = 22
  PLAN_CARTESIAN_TRAJ_CURRENT_TO_DES_TOOL_POSE = 23
  PLAN_CARTESIAN_TRAJ_QSTART_TO_DES_TOOL_POSE = 24
  PLAN_CARTESIAN_TRAJ_QPREV_TO_DES_TOOL_POSE = 25
  CLEAR_MULTI_TRAJ_PLAN = 26
  APPEND_MULTI_TRAJ_CART_SEGMENT = 27
  APPEND_MULTI_TRAJ_JSPACE_SEGMENT = 28
  TEST_PATH_FOR_DISCONTINUITIES = 29
  GET_NUM_PATH_SEGMENTS = 30
  GET_REPLANNED_ARRIVAL_TIMES = 31
  REPLAN_DISCONTINUITIES = 32
  REFINE_PLANNED_TRAJECTORY = 41
  SEGMENT_DISCONTINUOUS_TRAJ = 42
  EXECUTE_PLANNED_TRAJ = 100
  EXECUTE_TRAJ_NSEG = 101
  GOTO_NSEG_START = 102

  __slots__ = ['command_code','des_pose_gripper','arm_dp','q_goal','q_start','nsteps','arrival_time','nseg']
  _slot_types = ['int32','geometry_msgs/PoseStamped','float64[]','float64[]','float64[]','int32','float64','int32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       command_code,des_pose_gripper,arm_dp,q_goal,q_start,nsteps,arrival_time,nseg

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(arm_interfaceGoal, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.command_code is None:
        self.command_code = 0
      if self.des_pose_gripper is None:
        self.des_pose_gripper = geometry_msgs.msg.PoseStamped()
      if self.arm_dp is None:
        self.arm_dp = []
      if self.q_goal is None:
        self.q_goal = []
      if self.q_start is None:
        self.q_start = []
      if self.nsteps is None:
        self.nsteps = 0
      if self.arrival_time is None:
        self.arrival_time = 0.
      if self.nseg is None:
        self.nseg = 0
    else:
      self.command_code = 0
      self.des_pose_gripper = geometry_msgs.msg.PoseStamped()
      self.arm_dp = []
      self.q_goal = []
      self.q_start = []
      self.nsteps = 0
      self.arrival_time = 0.
      self.nseg = 0

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
      buff.write(_get_struct_i3I().pack(_x.command_code, _x.des_pose_gripper.header.seq, _x.des_pose_gripper.header.stamp.secs, _x.des_pose_gripper.header.stamp.nsecs))
      _x = self.des_pose_gripper.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_7d().pack(_x.des_pose_gripper.pose.position.x, _x.des_pose_gripper.pose.position.y, _x.des_pose_gripper.pose.position.z, _x.des_pose_gripper.pose.orientation.x, _x.des_pose_gripper.pose.orientation.y, _x.des_pose_gripper.pose.orientation.z, _x.des_pose_gripper.pose.orientation.w))
      length = len(self.arm_dp)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.arm_dp))
      length = len(self.q_goal)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.q_goal))
      length = len(self.q_start)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.q_start))
      _x = self
      buff.write(_get_struct_idi().pack(_x.nsteps, _x.arrival_time, _x.nseg))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.des_pose_gripper is None:
        self.des_pose_gripper = geometry_msgs.msg.PoseStamped()
      end = 0
      _x = self
      start = end
      end += 16
      (_x.command_code, _x.des_pose_gripper.header.seq, _x.des_pose_gripper.header.stamp.secs, _x.des_pose_gripper.header.stamp.nsecs,) = _get_struct_i3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.des_pose_gripper.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.des_pose_gripper.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 56
      (_x.des_pose_gripper.pose.position.x, _x.des_pose_gripper.pose.position.y, _x.des_pose_gripper.pose.position.z, _x.des_pose_gripper.pose.orientation.x, _x.des_pose_gripper.pose.orientation.y, _x.des_pose_gripper.pose.orientation.z, _x.des_pose_gripper.pose.orientation.w,) = _get_struct_7d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.arm_dp = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.q_goal = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.q_start = s.unpack(str[start:end])
      _x = self
      start = end
      end += 16
      (_x.nsteps, _x.arrival_time, _x.nseg,) = _get_struct_idi().unpack(str[start:end])
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
      buff.write(_get_struct_i3I().pack(_x.command_code, _x.des_pose_gripper.header.seq, _x.des_pose_gripper.header.stamp.secs, _x.des_pose_gripper.header.stamp.nsecs))
      _x = self.des_pose_gripper.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_7d().pack(_x.des_pose_gripper.pose.position.x, _x.des_pose_gripper.pose.position.y, _x.des_pose_gripper.pose.position.z, _x.des_pose_gripper.pose.orientation.x, _x.des_pose_gripper.pose.orientation.y, _x.des_pose_gripper.pose.orientation.z, _x.des_pose_gripper.pose.orientation.w))
      length = len(self.arm_dp)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.arm_dp.tostring())
      length = len(self.q_goal)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.q_goal.tostring())
      length = len(self.q_start)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.q_start.tostring())
      _x = self
      buff.write(_get_struct_idi().pack(_x.nsteps, _x.arrival_time, _x.nseg))
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
      if self.des_pose_gripper is None:
        self.des_pose_gripper = geometry_msgs.msg.PoseStamped()
      end = 0
      _x = self
      start = end
      end += 16
      (_x.command_code, _x.des_pose_gripper.header.seq, _x.des_pose_gripper.header.stamp.secs, _x.des_pose_gripper.header.stamp.nsecs,) = _get_struct_i3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.des_pose_gripper.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.des_pose_gripper.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 56
      (_x.des_pose_gripper.pose.position.x, _x.des_pose_gripper.pose.position.y, _x.des_pose_gripper.pose.position.z, _x.des_pose_gripper.pose.orientation.x, _x.des_pose_gripper.pose.orientation.y, _x.des_pose_gripper.pose.orientation.z, _x.des_pose_gripper.pose.orientation.w,) = _get_struct_7d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.arm_dp = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.q_goal = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.q_start = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      _x = self
      start = end
      end += 16
      (_x.nsteps, _x.arrival_time, _x.nseg,) = _get_struct_idi().unpack(str[start:end])
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
_struct_i3I = None
def _get_struct_i3I():
    global _struct_i3I
    if _struct_i3I is None:
        _struct_i3I = struct.Struct("<i3I")
    return _struct_i3I
_struct_idi = None
def _get_struct_idi():
    global _struct_idi
    if _struct_idi is None:
        _struct_idi = struct.Struct("<idi")
    return _struct_idi
