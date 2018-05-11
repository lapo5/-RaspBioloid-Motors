#!/usr/bin/env python

import rospy
import sys
sys.path.append(sys.path[0]+"/../src/python/dynamixel_functions_py/")
import dynamixel_workbench as dw
from motors.msg import *

def motor_monitor():
	rospy.init_node('motor_monitor', anonymous=True)

	pub = rospy.Publisher('motors_info', Motor, queue_size=100)

	workbench = dw.DynamixelWorkbench()
	workbench.begin("/dev/ttyACM0", 1000000)
	isOK, cont, ids = workbench.scan(18)
	motor_msg = MotorMsg()

	rate = rospy.Rate(1000)
	while not rospy.is_shutdown():
		isOk, positions = workbench.readAllPresentPosition(cont)
		isOk2, speeds = workbench.readAllPresentSpeed(cont)
		isOk3, voltages = workbench.readAllPresentVoltage(cont)
		isOk4, temperatures = workbench.readAllPresentTemperature(cont)
		
		if(isOk == True and isOk2 == True and isOk3 == True and isOk4 == True):
			motor_msg.Pos1 = positions[0]
			motor_msg.Pos2 = positions[1]
			motor_msg.Pos3 = positions[2]
			motor_msg.Pos4 = positions[3]
			motor_msg.Pos5 = positions[4]
			motor_msg.Pos6 = positions[5]
			motor_msg.Pos7 = positions[6]
			motor_msg.Pos8 = positions[7]
			motor_msg.Pos9 = positions[8]
			motor_msg.Pos10 = positions[9]
			motor_msg.Pos11 = positions[10]
			motor_msg.Pos12 = positions[11]
			motor_msg.Pos13 = positions[12]
			motor_msg.Pos14 = positions[13]
			motor_msg.Pos15 = positions[14]
			motor_msg.Pos16 = positions[15]
			motor_msg.Pos17 = positions[16]
			motor_msg.Pos18 = positions[17]
			motor_msg.Speed1 = speeds[0]
			motor_msg.Speed2 = speeds[1]
			motor_msg.Speed3 = speeds[2]
			motor_msg.Speed4 = speeds[3]
			motor_msg.Speed5 = speeds[4]
			motor_msg.Speed6 = speeds[5]
			motor_msg.Speed7 = speeds[6]
			motor_msg.Speed8 = speeds[7]
			motor_msg.Speed9 = speeds[8]
			motor_msg.Speed10 = speeds[9]
			motor_msg.Speed11 = speeds[10]
			motor_msg.Speed12 = speeds[11]
			motor_msg.Speed13 = speeds[12]
			motor_msg.Speed14 = speeds[13]
			motor_msg.Speed15 = speeds[14]
			motor_msg.Speed16 = speeds[15]
			motor_msg.Speed17 = speeds[16]
			motor_msg.Speed18 = speeds[17]
			motor_msg.Voltage1 = voltages[0]
			motor_msg.Voltage2 = voltages[1]
			motor_msg.Voltage3 = voltages[2]
			motor_msg.Voltage4 = voltages[3]
			motor_msg.Voltage5 = voltages[4]
			motor_msg.Voltage6 = voltages[5]
			motor_msg.Voltage7 = voltages[6]
			motor_msg.Voltage8 = voltages[7]
			motor_msg.Voltage9 = voltages[8]
			motor_msg.Voltage10 = voltages[9]
			motor_msg.Voltage11 = voltages[10]
			motor_msg.Voltage12 = voltages[11]
			motor_msg.Voltage13 = voltages[12]
			motor_msg.Voltage14 = voltages[13]
			motor_msg.Voltage15 = voltages[14]
			motor_msg.Voltage16 = voltages[15]
			motor_msg.Voltage17 = voltages[16]
			motor_msg.Voltage18 = voltages[17]
			motor_msg.Temperature1 = temperatures[0]
			motor_msg.Temperature2 = temperatures[1]
			motor_msg.Temperature3 = temperatures[2]
			motor_msg.Temperature4 = temperatures[3]
			motor_msg.Temperature5 = temperatures[4]
			motor_msg.Temperature6 = temperatures[5]
			motor_msg.Temperature7 = temperatures[6]
			motor_msg.Temperature8 = temperatures[7]
			motor_msg.Temperature9 = temperatures[8]
			motor_msg.Temperature10 = temperatures[9]
			motor_msg.Temperature11 = temperatures[10]
			motor_msg.Temperature12 = temperatures[11]
			motor_msg.Temperature13 = temperatures[12]
			motor_msg.Temperature14 = temperatures[13]
			motor_msg.Temperature15 = temperatures[14]
			motor_msg.Temperature16 = temperatures[15]
			motor_msg.Temperature17 = temperatures[16]
			motor_msg.Temperature18 = temperatures[17]

			#rospy.loginfo(motor_msg)
			pub.publish(motor_msg)
		rate.sleep()


	# spin() simply keeps python from exiting until this node is stopped
	rospy.spin()

if __name__ == '__main__':
	motor_monitor()
