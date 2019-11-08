#!/usr/bin/env python
import sys
import rospy
from om_aiv_util.srv import *
def getDataStoreTripGroupList_client(x):
    rospy.wait_for_service('getDataStoreTripGroupList')
    try:
        add_two_ints = rospy.ServiceProxy('getDataStoreTripGroupList', Service)
        resp1 = add_two_ints(x)
        return resp1.device
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "%s"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 1:
        x = ""
    else:
        print usage()
        sys.exit(1)
    print "running command"
    # print "Requesting", x
    print getDataStoreTripGroupList_client(x)
