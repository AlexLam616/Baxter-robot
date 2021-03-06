# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from baxter_core_msgs/HeadState.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class HeadState(genpy.Message):
  _md5sum = "71c43b264307205358e7e49be5601348"
  _type = "baxter_core_msgs/HeadState"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """float32 pan
bool isTurning
bool isNodding
bool isPanEnabled
"""
  __slots__ = ['pan','isTurning','isNodding','isPanEnabled']
  _slot_types = ['float32','bool','bool','bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       pan,isTurning,isNodding,isPanEnabled

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(HeadState, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.pan is None:
        self.pan = 0.
      if self.isTurning is None:
        self.isTurning = False
      if self.isNodding is None:
        self.isNodding = False
      if self.isPanEnabled is None:
        self.isPanEnabled = False
    else:
      self.pan = 0.
      self.isTurning = False
      self.isNodding = False
      self.isPanEnabled = False

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
      buff.write(_get_struct_f3B().pack(_x.pan, _x.isTurning, _x.isNodding, _x.isPanEnabled))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 7
      (_x.pan, _x.isTurning, _x.isNodding, _x.isPanEnabled,) = _get_struct_f3B().unpack(str[start:end])
      self.isTurning = bool(self.isTurning)
      self.isNodding = bool(self.isNodding)
      self.isPanEnabled = bool(self.isPanEnabled)
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
      buff.write(_get_struct_f3B().pack(_x.pan, _x.isTurning, _x.isNodding, _x.isPanEnabled))
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
      end = 0
      _x = self
      start = end
      end += 7
      (_x.pan, _x.isTurning, _x.isNodding, _x.isPanEnabled,) = _get_struct_f3B().unpack(str[start:end])
      self.isTurning = bool(self.isTurning)
      self.isNodding = bool(self.isNodding)
      self.isPanEnabled = bool(self.isPanEnabled)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_f3B = None
def _get_struct_f3B():
    global _struct_f3B
    if _struct_f3B is None:
        _struct_f3B = struct.Struct("<f3B")
    return _struct_f3B
