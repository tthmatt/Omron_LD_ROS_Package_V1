;; Auto-generated. Do not edit!


(when (boundp 'om_aiv_navigation::PatrolOnceResult)
  (if (not (find-package "OM_AIV_NAVIGATION"))
    (make-package "OM_AIV_NAVIGATION"))
  (shadow 'PatrolOnceResult (find-package "OM_AIV_NAVIGATION")))
(unless (find-package "OM_AIV_NAVIGATION::PATROLONCERESULT")
  (make-package "OM_AIV_NAVIGATION::PATROLONCERESULT"))

(in-package "ROS")
;;//! \htmlinclude PatrolOnceResult.msg.html


(defclass om_aiv_navigation::PatrolOnceResult
  :super ros::object
  :slots (_status ))

(defmethod om_aiv_navigation::PatrolOnceResult
  (:init
   (&key
    ((:status __status) "")
    )
   (send-super :init)
   (setq _status (string __status))
   self)
  (:status
   (&optional __status)
   (if __status (setq _status __status)) _status)
  (:serialization-length
   ()
   (+
    ;; string _status
    4 (length _status)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _status
       (write-long (length _status) s) (princ _status s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _status
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _status (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get om_aiv_navigation::PatrolOnceResult :md5sum-) "4fe5af303955c287688e7347e9b00278")
(setf (get om_aiv_navigation::PatrolOnceResult :datatype-) "om_aiv_navigation/PatrolOnceResult")
(setf (get om_aiv_navigation::PatrolOnceResult :definition-)
      "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
# Result
string status


")



(provide :om_aiv_navigation/PatrolOnceResult "4fe5af303955c287688e7347e9b00278")

