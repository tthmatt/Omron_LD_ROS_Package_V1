#!/usr/bin/env python
import sys
import rospy
from om_aiv_util.srv import *
def say_client(array):
    rospy.wait_for_service('say')
    try:
        service = rospy.ServiceProxy('say', OmAivService)
        resp1 = service(array)
        return resp1.device
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "%s <text_string>"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 2:
        text_str = str(sys.argv[1])
        array = [text_str]
    else:
        print usage()
        sys.exit(1)
    print "running command"
    print say_client(array)
