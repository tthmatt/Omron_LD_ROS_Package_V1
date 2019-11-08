#!/usr/bin/env python
import sys
import rospy
from om_aiv_util.srv import *
def outputOn_client(a):
    rospy.wait_for_service('outputOn')
    try:
        add_two_ints = rospy.ServiceProxy('outputOn', Service)
        resp1 = add_two_ints(a)
        return resp1.device
    except rospy.ServiceException, error:
        print "Service call failed: %s"%error

def usage():
    return "%s <name>"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 2:
        a = str(sys.argv[1])
    else:
        print usage()
        sys.exit(1)
    print "running command"
    # print "Requesting", x
    print outputOn_client(a)