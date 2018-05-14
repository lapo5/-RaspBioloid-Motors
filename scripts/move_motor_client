#!/usr/bin/env python

import sys
import rospy
from motors.srv import *

def move_motor_client(mytype):
	if(mytype == 0):
		rospy.wait_for_service('move_motor')
		try:
			move_motor = rospy.ServiceProxy('move_motor', MoveMotor)
			resp1 = move_motor(1, 15, 125)
			return resp1.result
		except rospy.ServiceException, e:
			print "Service call failed: %s"%e
	if(mytype == 1):
		rospy.wait_for_service('torque_motor')
		try:
			torque_motor = rospy.ServiceProxy('torque_motor', Torque)
			resp1 = torque_motor(13, 0)
			return resp1.result
		except rospy.ServiceException, e:
			print "Service call failed: %s"%e
	if(mytype == 2):
		rospy.wait_for_service('torque_all')
		try:
			torque_all = rospy.ServiceProxy('torque_all', TorqueAll)
			resp1 = torque_all(1)
			return resp1.result
		except rospy.ServiceException, e:
			print "Service call failed: %s"%e



if __name__ == "__main__":
    if len(sys.argv) == 2:
		mytype = int(sys.argv[1])
    else:
        sys.exit(1)
    print "Requesting sevrice"
    print "Returned %d" % move_motor_client(mytype)
