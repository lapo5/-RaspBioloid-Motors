#!/usr/bin/env python

from motors.srv import *
import rospy, sys
sys.path.append(sys.path[0]+"/../src/python/dynamixel_functions_py/")
import dynamixel_workbench as dw

workbench = dw.DynamixelWorkbench()
workbench.begin("/dev/ttyACM0", 1000000)
isTotallyOK, cont, ids = workbench.scan(18)

def move_motor(req):
	print("Moving motor {0} to position {1} with velocity {2}".format(req.id, req.pos, req.vel))
	return MoveMotorResponse(1001)

def torque_motor(req):
	isOk = workbench.torque(req.id, req.mode)
	return TorqueResponse(isOk)

def torque_all(req):
	isOk = workbench.torqueAll(cont, req.mode)
	return TorqueAllResponse(isOk)


def motor_server():
	rospy.init_node('motor_server')

	if(isTotallyOK == False):
		print("Error")
	else:
		s1 = rospy.Service('move_motor', MoveMotor, move_motor)
		s2 = rospy.Service('torque_motor', Torque, torque_motor)
		s3 = rospy.Service('torque_all', TorqueAll, torque_all)
		rospy.spin()

if __name__ == "__main__":
	motor_server()


