; Auto-generated. Do not edit!


(cl:in-package object_grabber-msg)


;//! \htmlinclude object_grabberFeedback.msg.html

(cl:defclass <object_grabberFeedback> (roslisp-msg-protocol:ros-message)
  ((fdbk
    :reader fdbk
    :initarg :fdbk
    :type cl:integer
    :initform 0))
)

(cl:defclass object_grabberFeedback (<object_grabberFeedback>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <object_grabberFeedback>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'object_grabberFeedback)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name object_grabber-msg:<object_grabberFeedback> is deprecated: use object_grabber-msg:object_grabberFeedback instead.")))

(cl:ensure-generic-function 'fdbk-val :lambda-list '(m))
(cl:defmethod fdbk-val ((m <object_grabberFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader object_grabber-msg:fdbk-val is deprecated.  Use object_grabber-msg:fdbk instead.")
  (fdbk m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <object_grabberFeedback>) ostream)
  "Serializes a message object of type '<object_grabberFeedback>"
  (cl:let* ((signed (cl:slot-value msg 'fdbk)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <object_grabberFeedback>) istream)
  "Deserializes a message object of type '<object_grabberFeedback>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'fdbk) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<object_grabberFeedback>)))
  "Returns string type for a message object of type '<object_grabberFeedback>"
  "object_grabber/object_grabberFeedback")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'object_grabberFeedback)))
  "Returns string type for a message object of type 'object_grabberFeedback"
  "object_grabber/object_grabberFeedback")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<object_grabberFeedback>)))
  "Returns md5sum for a message object of type '<object_grabberFeedback>"
  "46cc8f8da6ebf35aedc6bad2e96b2e59")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'object_grabberFeedback)))
  "Returns md5sum for a message object of type 'object_grabberFeedback"
  "46cc8f8da6ebf35aedc6bad2e96b2e59")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<object_grabberFeedback>)))
  "Returns full string definition for message of type '<object_grabberFeedback>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%#feedback: optional; ~%~%int32 fdbk~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'object_grabberFeedback)))
  "Returns full string definition for message of type 'object_grabberFeedback"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%#feedback: optional; ~%~%int32 fdbk~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <object_grabberFeedback>))
  (cl:+ 0
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <object_grabberFeedback>))
  "Converts a ROS message object to a list"
  (cl:list 'object_grabberFeedback
    (cl:cons ':fdbk (fdbk msg))
))
