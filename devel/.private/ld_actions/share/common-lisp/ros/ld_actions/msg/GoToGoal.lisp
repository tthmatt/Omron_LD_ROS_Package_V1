; Auto-generated. Do not edit!


(cl:in-package ld_actions-msg)


;//! \htmlinclude GoToGoal.msg.html

(cl:defclass <GoToGoal> (roslisp-msg-protocol:ros-message)
  ((goal_goto
    :reader goal_goto
    :initarg :goal_goto
    :type cl:string
    :initform ""))
)

(cl:defclass GoToGoal (<GoToGoal>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <GoToGoal>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'GoToGoal)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ld_actions-msg:<GoToGoal> is deprecated: use ld_actions-msg:GoToGoal instead.")))

(cl:ensure-generic-function 'goal_goto-val :lambda-list '(m))
(cl:defmethod goal_goto-val ((m <GoToGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ld_actions-msg:goal_goto-val is deprecated.  Use ld_actions-msg:goal_goto instead.")
  (goal_goto m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <GoToGoal>) ostream)
  "Serializes a message object of type '<GoToGoal>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'goal_goto))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'goal_goto))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <GoToGoal>) istream)
  "Deserializes a message object of type '<GoToGoal>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'goal_goto) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'goal_goto) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<GoToGoal>)))
  "Returns string type for a message object of type '<GoToGoal>"
  "ld_actions/GoToGoal")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GoToGoal)))
  "Returns string type for a message object of type 'GoToGoal"
  "ld_actions/GoToGoal")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<GoToGoal>)))
  "Returns md5sum for a message object of type '<GoToGoal>"
  "25d262ea5119ec12857b9a886dcbb445")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'GoToGoal)))
  "Returns md5sum for a message object of type 'GoToGoal"
  "25d262ea5119ec12857b9a886dcbb445")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<GoToGoal>)))
  "Returns full string definition for message of type '<GoToGoal>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# Goal~%string goal_goto~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'GoToGoal)))
  "Returns full string definition for message of type 'GoToGoal"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# Goal~%string goal_goto~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <GoToGoal>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'goal_goto))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <GoToGoal>))
  "Converts a ROS message object to a list"
  (cl:list 'GoToGoal
    (cl:cons ':goal_goto (goal_goto msg))
))