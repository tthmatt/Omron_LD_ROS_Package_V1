#!/usr/bin/env python
import sys
import rospy
from om_aiv_util.srv import *
def queueModifyLocal_client(array):
    rospy.wait_for_service('queueModifyLocal')
    try:
        service = rospy.ServiceProxy('queueModifyLocal', OmAivService)
        resp1 = service(array)
        return resp1.device
    except rospy.ServiceException, error:
        print "Service call failed: %s"%error

def usage():
    return "%s <id> <type> <value>"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 4:
        id = str(sys.argv[1])
        type = str(sys.argv[2])
        value = str(sys.argv[3])
        array = [id, type, value]
    else:
        print usage()
        sys.exit(1)
    print "running command"
    print queueModifyLocal_client(array)
