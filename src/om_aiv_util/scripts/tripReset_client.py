#!/usr/bin/env python
import sys
import rospy
from om_aiv_util.srv import *
def tripReset_client():
    rospy.wait_for_service('tripReset')
    try:
        service = rospy.ServiceProxy('tripReset', OmAivService)
        resp1 = service()
        return resp1.device
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "%s"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 1:
        pass
    else:
        print usage()
        sys.exit(1)
    print "running command"
    print tripReset_client()
