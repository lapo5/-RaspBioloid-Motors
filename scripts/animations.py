#!/usr/bin/env python

import sys, time
import rospy
from motors_srvs.srv import *

def move_all_motors(pos, vel=90):
	rospy.wait_for_service('move_motor')
	try:
		move_motor = rospy.ServiceProxy('move_motor', MoveMotor)
		resp1 = move_motor(1, pos[0], vel)
		resp1 = move_motor(2, pos[1], vel)
		resp1 = move_motor(3, pos[2], vel)
		resp1 = move_motor(4, pos[3], vel)
		resp1 = move_motor(5, pos[4], vel)
		resp1 = move_motor(6, pos[5], vel)
		resp1 = move_motor(7, pos[6], vel)
		resp1 = move_motor(8, pos[7], vel)
		resp1 = move_motor(9, pos[8], vel)
		resp1 = move_motor(10, pos[9], vel)
		resp1 = move_motor(11, pos[10], vel)
		resp1 = move_motor(12, pos[11], vel)
		resp1 = move_motor(13, pos[12], vel)
		resp1 = move_motor(14, pos[13], vel)
		resp1 = move_motor(15, pos[14], vel)
		resp1 = move_motor(16, pos[15], vel)
		resp1 = move_motor(17, pos[16], vel)
		resp1 = move_motor(18, pos[17], vel)
	except rospy.ServiceException, e:
			print "Service call failed: %s"%e

def initial_position(vel = 60):
	move_motor = rospy.ServiceProxy('move_motor', MoveMotor)
	resp1 = move_motor(1, 210, vel)
	resp1 = move_motor(2, 814, vel)
	resp1 = move_motor(3, 292, vel)
	resp1 = move_motor(4, 732, vel)
	resp1 = move_motor(5, 484, vel)
	resp1 = move_motor(6, 540, vel)
	resp1 = move_motor(7, 355, vel)
	resp1 = move_motor(8, 669, vel)
	resp1 = move_motor(9, 496, vel)
	resp1 = move_motor(10, 527, vel)
	resp1 = move_motor(11, 512, vel)
	resp1 = move_motor(12, 512, vel)
	resp1 = move_motor(13, 520, vel)
	resp1 = move_motor(14, 504, vel)
	resp1 = move_motor(15, 504, vel)
	resp1 = move_motor(16, 520, vel)
	resp1 = move_motor(17, 500, vel)
	resp1 = move_motor(18, 524, vel)

def say_hello():
	move_motor = rospy.ServiceProxy('move_motor', MoveMotor)
	resp1 = move_motor(2, 380, 80)
	time.sleep(1)
	resp1 = move_motor(4, 590, 80)
	time.sleep(1)
	resp1 = move_motor(6, 635, 80)
	for i in range(0, 3):
		resp1 = move_motor(2, 326, 90)
		resp1 = move_motor(4, 700, 90)
		time.sleep(1)
		resp1 = move_motor(2, 380, 90)
		resp1 = move_motor(4, 590, 90)
		time.sleep(1)

	resp1 = move_motor(2, 814, 80)
	resp1 = move_motor(4, 732, 80)
	resp1 = move_motor(6, 540, 80)

def say_hello_2_hand():
	move_motor = rospy.ServiceProxy('move_motor', MoveMotor)
	resp1 = move_motor(2, 380, 80)
	resp1 = move_motor(1, 644, 80)
	time.sleep(1)
	resp1 = move_motor(3, 434, 80)
	resp1 = move_motor(4, 590, 80)
	time.sleep(1)
	resp1 = move_motor(5, 389, 80)
	resp1 = move_motor(6, 635, 80)
	for i in range(0, 3):
		resp1 = move_motor(2, 326, 90)
		resp1 = move_motor(1, 689, 90)
		resp1 = move_motor(3, 324, 90)
		resp1 = move_motor(4, 700, 90)
		time.sleep(1)
		resp1 = move_motor(1, 644, 90)
		resp1 = move_motor(2, 380, 90)
		resp1 = move_motor(3, 434, 90)
		resp1 = move_motor(4, 590, 90)
		time.sleep(1)

	resp1 = move_motor(1, 210, 60)
	resp1 = move_motor(2, 814, 60)
	resp1 = move_motor(3, 292, 60)
	resp1 = move_motor(4, 732, 60)
	resp1 = move_motor(5, 484, 60)
	resp1 = move_motor(6, 540, 60)

def stand_down():
	move_motor = rospy.ServiceProxy('move_motor', MoveMotor)

	pos = [210, 814, 292, 732, 484, 540, 355, 669, 508, 515, 512, 512, 520, 504, 512, 512, 500, 524]
	move_all_motors(pos)
	resp1 = move_motor(13, 450, 60)
	resp1 = move_motor(14, 571, 60)
	resp1 = move_motor(15, 577, 60)
	resp1 = move_motor(16, 447, 60)
	resp1 = move_motor(11, 594, 60)
	resp1 = move_motor(12, 430, 60)

	time.sleep(0.2)

	resp1 = move_motor(13, 323, 40)
	resp1 = move_motor(14, 701, 40)
	resp1 = move_motor(15, 660, 40)
	resp1 = move_motor(16, 364, 40)
	resp1 = move_motor(11, 594, 40)
	resp1 = move_motor(12, 430, 40)

	time.sleep(1.5)

	resp1 = move_motor(11, 359, 40)
	resp1 = move_motor(12, 665, 40)
	time.sleep(1)
	resp1 = move_motor(13, 180, 40)
	resp1 = move_motor(14, 844, 40)
	time.sleep(0.5)

	resp1 = move_motor(15, 689, 60)
	resp1 = move_motor(16, 335, 60)
	time.sleep(3)

	resp1 = move_motor(11, 300, 40)
	resp1 = move_motor(12, 724, 40)
	time.sleep(2)
	resp1 = move_motor(11, 273, 40)
	resp1 = move_motor(12, 751, 40)
	resp1 = move_motor(13, 100, 40)
	resp1 = move_motor(14, 934, 40)
	resp1 = move_motor(15, 700, 40)
	resp1 = move_motor(16, 314, 40)
	time.sleep(1)
	resp1 = move_motor(13, 70, 40)
	resp1 = move_motor(14, 964, 40)
	time.sleep(1)
	resp1 = move_motor(15, 760, 40)
	resp1 = move_motor(16, 284, 40)
	resp1 = move_motor(11, 273, 40)
	resp1 = move_motor(12, 751, 40)

def from_initial_to_walk():
	move_motor = rospy.ServiceProxy('move_motor', MoveMotor)

	pos = [210, 814, 292, 732, 484, 540, 355, 669, 508, 515, 512, 512, 520, 504, 512, 512, 500, 524]
	move_all_motors(pos)
	resp1 = move_motor(13, 450, 60)
	resp1 = move_motor(14, 571, 60)
	resp1 = move_motor(15, 577, 60)
	resp1 = move_motor(16, 447, 60)
	resp1 = move_motor(11, 594, 60)
	resp1 = move_motor(12, 430, 60)

	time.sleep(0.2)

	resp1 = move_motor(13, 323, 40)
	resp1 = move_motor(14, 701, 40)
	resp1 = move_motor(15, 660, 40)
	resp1 = move_motor(16, 364, 40)
	resp1 = move_motor(11, 594, 40)
	resp1 = move_motor(12, 430, 40)

	time.sleep(1.5)

	resp1 = move_motor(11, 359, 40)
	resp1 = move_motor(12, 665, 40)
	time.sleep(1)
	resp1 = move_motor(13, 180, 40)
	resp1 = move_motor(14, 844, 40)
	time.sleep(0.5)

	resp1 = move_motor(15, 689, 60)
	resp1 = move_motor(16, 335, 60)
	time.sleep(3)

def from_walk_to_initial():
	move_motor = rospy.ServiceProxy('move_motor', MoveMotor)

	pos = [235, 788, 279, 744, 462, 561, 358, 666, 513, 522, 342, 681, 241, 781, 646, 377, 513, 522]
	move_all_motors(pos)
	time.sleep(2)

	resp1 = move_motor(11, 360, 40)
	resp1 = move_motor(12, 664, 40)

	resp1 = move_motor(13, 250, 40)
	resp1 = move_motor(14, 774, 40)

	time.sleep(0.8)

	resp1 = move_motor(11, 380, 40)
	resp1 = move_motor(12, 644, 40)

	resp1 = move_motor(13, 270, 40)
	resp1 = move_motor(14, 754, 40)

	time.sleep(0.8)
	resp1 = move_motor(11, 400, 40)
	resp1 = move_motor(12, 624, 40)

	resp1 = move_motor(13, 290, 40)
	resp1 = move_motor(14, 734, 40)

	time.sleep(0.8)
	resp1 = move_motor(11, 420, 40)
	resp1 = move_motor(12, 604, 40)

	resp1 = move_motor(13, 310, 40)
	resp1 = move_motor(14, 714, 40)
	resp1 = move_motor(15, 624, 40)
	resp1 = move_motor(16, 400, 40)


	time.sleep(0.8)
	resp1 = move_motor(11, 460, 40)
	resp1 = move_motor(12, 564, 40)

	resp1 = move_motor(13, 350, 40)
	resp1 = move_motor(14, 674, 40)
	resp1 = move_motor(15, 604, 40)
	resp1 = move_motor(16, 420, 40)

	time.sleep(0.8)
	resp1 = move_motor(11, 480, 40)
	resp1 = move_motor(12, 544, 40)
	resp1 = move_motor(13, 370, 40)
	resp1 = move_motor(14, 654, 40)

	time.sleep(0.8)
	resp1 = move_motor(11, 500, 40)
	resp1 = move_motor(12, 524, 40)
	resp1 = move_motor(13, 390, 40)
	resp1 = move_motor(14, 634, 40)

	time.sleep(0.8)

	resp1 = move_motor(13, 410, 40)
	resp1 = move_motor(14, 614, 40)
	resp1 = move_motor(15, 584, 40)
	resp1 = move_motor(16, 440, 40)
	resp1 = move_motor(11, 480, 40)
	resp1 = move_motor(12, 544, 40)

	time.sleep(0.8)

	resp1 = move_motor(13, 430, 40)
	resp1 = move_motor(14, 594, 40)
	resp1 = move_motor(15, 564, 40)
	resp1 = move_motor(16, 460, 40)
	resp1 = move_motor(11, 460, 40)
	resp1 = move_motor(12, 564, 40)

	time.sleep(0.8)

	resp1 = move_motor(13, 450, 40)
	resp1 = move_motor(14, 574, 40)
	resp1 = move_motor(15, 544, 40)
	resp1 = move_motor(16, 480, 40)
	resp1 = move_motor(11, 440, 40)
	resp1 = move_motor(12, 584, 40)

	time.sleep(0.8)

	resp1 = move_motor(13, 470, 40)
	resp1 = move_motor(14, 554, 40)
	resp1 = move_motor(15, 524, 40)
	resp1 = move_motor(16, 500, 40)
	resp1 = move_motor(11, 460, 40)
	resp1 = move_motor(12, 564, 40)


	time.sleep(0.8)

	resp1 = move_motor(13, 490, 40)
	resp1 = move_motor(14, 534, 40)
	resp1 = move_motor(15, 512, 40)
	resp1 = move_motor(16, 512, 40)
	resp1 = move_motor(11, 480, 40)
	resp1 = move_motor(12, 584, 40)

	initial_position()

def stand_up():
	move_motor = rospy.ServiceProxy('move_motor', MoveMotor)
	resp1 = move_motor(15, 760, 40)
	resp1 = move_motor(16, 284, 40)
	resp1 = move_motor(11, 273, 40)
	resp1 = move_motor(12, 751, 40)

	resp1 = move_motor(13, 70, 40)
	resp1 = move_motor(14, 964, 40)

	time.sleep(2)

	resp1 = move_motor(15, 700, 40)
	resp1 = move_motor(16, 314, 40)
	resp1 = move_motor(11, 273, 40)
	resp1 = move_motor(12, 751, 40)

	time.sleep(1)

	resp1 = move_motor(15, 689, 60)
	resp1 = move_motor(16, 335, 60)
	time.sleep(1)
	resp1 = move_motor(13, 180, 40)
	resp1 = move_motor(14, 844, 40)
	time.sleep(1)
	resp1 = move_motor(11, 300, 40)
	resp1 = move_motor(12, 724, 40)
	time.sleep(1)

	resp1 = move_motor(13, 270, 40)
	resp1 = move_motor(14, 754, 40)

	resp1 = move_motor(15, 605, 40)
	resp1 = move_motor(16, 419, 40)

	time.sleep(3)

	resp1 = move_motor(11, 450, 40)
	resp1 = move_motor(12, 574, 40)

	resp1 = move_motor(13, 370, 40)
	resp1 = move_motor(14, 654, 40)

	time.sleep(3)

	resp1 = move_motor(15, 585, 40)
	resp1 = move_motor(16, 439, 40)
	resp1 = move_motor(11, 430, 40)
	resp1 = move_motor(12, 594, 40)
	resp1 = move_motor(13, 390, 40)
	resp1 = move_motor(14, 634, 40)

	time.sleep(1)

	resp1 = move_motor(15, 565, 40)
	resp1 = move_motor(16, 459, 40)
	resp1 = move_motor(11, 410, 40)
	resp1 = move_motor(12, 614, 40)
	resp1 = move_motor(13, 410, 40)
	resp1 = move_motor(14, 614, 40)

	time.sleep(1)

	resp1 = move_motor(15, 545, 40)
	resp1 = move_motor(16, 479, 40)
	resp1 = move_motor(11, 390, 40)
	resp1 = move_motor(12, 634, 40)
	resp1 = move_motor(13, 430, 40)
	resp1 = move_motor(14, 594, 40)

	time.sleep(1)

	resp1 = move_motor(11, 410, 40)
	resp1 = move_motor(12, 614, 40)
	resp1 = move_motor(13, 450, 40)
	resp1 = move_motor(14, 574, 40)
	time.sleep(1)

	resp1 = move_motor(11, 460, 40)
	resp1 = move_motor(12, 564, 40)
	resp1 = move_motor(13, 470, 40)
	resp1 = move_motor(14, 554, 40)

	time.sleep(1)

	resp1 = move_motor(11, 490, 40)
	resp1 = move_motor(12, 534, 40)
	resp1 = move_motor(13, 490, 40)
	resp1 = move_motor(14, 534, 40)

	time.sleep(1)

	resp1 = move_motor(11, 512, 30)
	resp1 = move_motor(12, 512, 30)
	resp1 = move_motor(15, 524, 30)
	resp1 = move_motor(16, 500, 30)
	resp1 = move_motor(13, 520, 30)
	resp1 = move_motor(14, 504, 30)

	time.sleep(3)

	resp1 = move_motor(11, 512, 30)
	resp1 = move_motor(12, 512, 30)
	resp1 = move_motor(13, 520, 30)
	resp1 = move_motor(14, 504, 30)
	resp1 = move_motor(15, 504, 30)
	resp1 = move_motor(16, 520, 30)

	initial_position(40)

def gorilla():
	move_motor = rospy.ServiceProxy('move_motor', MoveMotor)
	#OPEN ARMS
	pos = [552, 471, 424, 599, 159, 864, 355, 669, 508, 515, 512, 512, 520, 504, 512, 512, 500, 524]
	move_all_motors(pos)

	for i in range(0,3):
		#MOVE RIGHT ARM
		resp1 = move_motor(3, 238, 150)
		resp1 = move_motor(4, 599, 150)
		resp1 = move_motor(5, 150, 150)
		resp1 = move_motor(6, 874, 150)
		time.sleep(0.7)
		#MOVE LEFT ARM
		resp1 = move_motor(3, 424, 150)
		resp1 = move_motor(4, 786, 150)
		resp1 = move_motor(5, 170, 150)
		resp1 = move_motor(6, 855, 150)
		time.sleep(0.7)

	pos = [552, 471, 424, 599, 159, 864, 355, 669, 508, 515, 512, 512, 520, 504, 512, 512, 500, 524]
	move_all_motors(pos)

	resp1 = move_motor(1, 210, 60)
	resp1 = move_motor(2, 814, 60)
	resp1 = move_motor(3, 292, 60)
	resp1 = move_motor(4, 732, 60)
	resp1 = move_motor(5, 484, 60)
	resp1 = move_motor(6, 540, 60)

def walk():
	pos = [235, 788, 279, 744, 462, 561, 358, 666, 513, 522, 342, 681, 241, 781, 646, 377, 513, 522]
	move_all_motors(pos)
	time.sleep(2)
	pos = [235, 788, 279, 744, 462, 561, 358, 666, 519, 528, 344, 678, 245, 776, 644, 380, 519, 528]
	move_all_motors(pos)
	pos = [235, 788, 279, 744, 462, 561, 358, 666, 524, 533, 346, 675, 250, 770, 642, 383, 524, 533]
	move_all_motors(pos)
	pos = [235, 788, 279, 744, 462, 561, 358, 666, 528, 537, 349, 672, 256, 763, 639, 386, 528, 537]
	move_all_motors(pos)
	pos = [235, 788, 279, 744, 462, 561, 358, 666, 521, 544, 352, 679, 262, 778, 636, 379, 531, 541]
	move_all_motors(pos)
	pos = [235, 788, 279, 744, 462, 561, 358, 666, 503, 555, 354, 696, 266, 811, 634, 362, 533, 544]
	move_all_motors(pos)
	pos = [235, 788, 279, 744, 462, 561, 358, 666, 494, 560, 355, 703, 268, 826, 633, 355, 534, 546]
	move_all_motors(pos)
	pos = [233, 786, 279, 744, 462, 561, 358, 666, 503, 555, 353, 725, 267, 807, 641, 386, 533, 544]
	move_all_motors(pos)
	pos = [248, 801, 279, 744, 462, 561, 358, 666, 521, 544, 357, 718, 264, 765, 648, 421, 531, 541]
	move_all_motors(pos)
	pos = [263, 816, 279, 744, 462, 561, 358, 666, 528, 537, 355, 713, 259, 744, 652, 437, 528, 537]
	move_all_motors(pos)
	pos = [276, 829, 279, 744, 462, 561, 358, 666, 524, 533, 352, 718, 252, 751, 655, 434, 524, 533]
	move_all_motors(pos)
	pos = [287, 840, 279, 744, 462, 561, 358, 666, 519, 528, 353, 720, 248, 760, 660, 427, 519, 528]
	move_all_motors(pos)
	pos = [295, 848, 279, 744, 462, 561, 358, 666, 513, 522, 357, 719, 246, 769, 666, 418, 513, 522]
	move_all_motors(pos)
	pos = [301, 854, 279, 744, 462, 561, 358, 666, 507, 516, 364, 716, 248, 775, 671, 409, 507, 516]
	move_all_motors(pos)

	for i in range(0,4):

		pos = [300, 853, 279, 744, 462, 561, 358, 666, 501, 510, 363, 721, 254, 777, 675, 402, 501, 510]
		move_all_motors(pos)
		pos = [303, 856, 279, 744, 462, 561, 358, 666, 496, 505, 372, 715, 262, 775, 675, 398, 496, 505]
		move_all_motors(pos)
		pos = [302, 855, 279, 744, 462, 561, 358, 666, 490, 504, 373, 709, 262, 771, 677, 395, 491, 500]
		move_all_motors(pos)
		pos = [298, 851, 279, 744, 462, 561, 358, 666, 482, 510, 361, 702, 245, 766, 682, 394, 486, 496]
		move_all_motors(pos)
		pos = [290, 843, 279, 744, 462, 561, 358, 666, 473, 519, 341, 696, 222, 761, 685, 393, 482, 493]
		move_all_motors(pos)
		pos = [280, 833, 279, 744, 462, 561, 358, 666, 467, 527, 319, 691, 203, 757, 681, 392, 480, 491]
		move_all_motors(pos)
		pos = [268, 821, 279, 744, 462, 561, 358, 666, 465, 530, 299, 688, 196, 756, 669, 390, 479, 490]
		move_all_motors(pos)
		pos = [254, 807, 279, 744, 462, 561, 358, 666, 467, 527, 287, 686, 203, 757, 649, 387, 480, 491]
		move_all_motors(pos)
		pos = [239, 792, 279, 744, 462, 561, 358, 666, 473, 519, 283, 685, 222, 761, 627, 382, 482, 493]
		move_all_motors(pos)
		pos = [223, 776, 279, 744, 462, 561, 358, 666, 482, 510, 286, 684, 245, 766, 607, 376, 486, 496]
		move_all_motors(pos)
		pos = [209, 762, 279, 744, 462, 561, 358, 666, 490, 504, 291, 683, 262, 771, 595, 369, 491, 500]
		move_all_motors(pos)
		pos = [195, 748, 279, 744, 462, 561, 358, 666, 496, 505, 293, 680, 262, 775, 596, 363, 496, 505]
		move_all_motors(pos)
		pos = [184, 737, 279, 744, 462, 561, 358, 666, 501, 510, 293, 676, 254, 777, 605, 357, 501, 510]
		move_all_motors(pos)
		pos = [175, 728, 279, 744, 462, 561, 358, 666, 507, 516, 297, 669, 248, 775, 614, 352, 507, 516]
		move_all_motors(pos)

		pos = [169, 722, 279, 744, 462, 561, 358, 666, 513, 522, 302, 660, 246, 769, 621, 348, 513, 522]
		move_all_motors(pos)
		pos = [166, 719, 279, 744, 462, 561, 358, 666, 518, 527, 308, 651, 248, 761, 625, 348, 518, 527]
		move_all_motors(pos)
		pos = [167, 720, 279, 744, 462, 561, 358, 666, 519, 533, 314, 650, 252, 761, 628, 346, 523, 532]
		move_all_motors(pos)
		pos = [171, 724, 279, 744, 462, 561, 358, 666, 513, 541, 321, 662, 257, 778, 629, 341, 527, 537]
		move_all_motors(pos)
		pos = [179, 732, 279, 744, 462, 561, 358, 666, 504, 550, 327, 682, 262, 801, 630, 338, 530, 541]
		move_all_motors(pos)
		pos = [189, 742, 279, 744, 462, 561, 358, 666, 496, 556, 332, 704, 266, 820, 631, 342, 532, 543]
		move_all_motors(pos)
		pos = [201, 754, 279, 744, 462, 561, 358, 666, 493, 558, 335, 724, 267, 827, 633, 354, 533, 544]
		move_all_motors(pos)
		pos = [215, 768, 279, 744, 462, 561, 358, 666, 496, 556, 337, 736, 266, 820, 636, 374, 532, 543]
		move_all_motors(pos)
		pos = [230, 783, 279, 744, 462, 561, 358, 666, 504, 550, 338, 740, 262, 801, 641, 396, 530, 541]
		move_all_motors(pos)
		pos = [246, 799, 279, 744, 462, 561, 358, 666, 513, 541, 339, 737, 257, 778, 647, 416, 527, 537]
		move_all_motors(pos)
		pos = [260, 813, 279, 744, 462, 561, 358, 666, 519, 533, 340, 732, 252, 761, 654, 428, 523, 532]
		move_all_motors(pos)
		pos = [274, 827, 279, 744, 462, 561, 358, 666, 518, 527, 343, 730, 248, 761, 660, 427, 518, 527]
		move_all_motors(pos)
		pos = [285, 838, 279, 744, 462, 561, 358, 666, 513, 522, 347, 730, 246, 769, 666, 418, 513, 522]
		move_all_motors(pos)
		pos = [294, 847, 279, 744, 462, 561, 358, 666, 507, 516, 354, 726, 248, 775, 671, 409, 507, 516]
		move_all_motors(pos)

		time.sleep(0.5)

		pos = [235, 788, 279, 744, 462, 561, 358, 666, 513, 522, 342, 681, 241, 781, 646, 377, 513, 522]
		time.sleep(0.5)


	#EXIT SEQUENCE
	pos = [303, 856, 279, 744, 462, 561, 358, 666, 501, 510, 373, 711, 254, 777, 674, 402, 501, 510]
	move_all_motors(pos)
	pos = [301, 854, 279, 744, 462, 561, 358, 666, 495, 504, 382, 705, 263, 775, 675, 398, 495, 504]
	move_all_motors(pos)
	pos = [297, 850, 279, 744, 462, 561, 358, 666, 490, 499, 389, 700, 272, 771, 673, 397, 490, 499]
	move_all_motors(pos)
	pos = [289, 842, 279, 744, 462, 561, 358, 666, 486, 495, 392, 697, 279, 764, 668, 400, 486, 495]
	move_all_motors(pos)
	pos = [278, 831, 279, 744, 462, 561, 358, 666, 479, 502, 376, 693, 258, 759, 673, 402, 482, 492]
	move_all_motors(pos)
	pos = [265, 818, 279, 744, 462, 561, 358, 666, 468, 520, 341, 686, 216, 756, 680, 398, 479, 490]
	move_all_motors(pos)
	pos = [251, 804, 279, 744, 462, 561, 358, 666, 463, 529, 310, 678, 197, 755, 668, 390, 477, 489]
	move_all_motors(pos)
	pos = [235, 788, 279, 744, 462, 561, 358, 666, 468, 520, 327, 669, 212, 757, 661, 389, 479, 490]
	move_all_motors(pos)
	pos = [235, 788, 279, 744, 462, 561, 358, 666, 479, 502, 344, 671, 245, 761, 644, 387, 482, 492]
	move_all_motors(pos)
	pos = [235, 788, 279, 744, 462, 561, 358, 666, 486, 495, 351, 674, 260, 767, 637, 384, 486, 495]
	move_all_motors(pos)
	pos = [235, 788, 279, 744, 462, 561, 358, 666, 490, 499, 348, 677, 253, 773, 640, 381, 490, 499]
	move_all_motors(pos)
	pos = [235, 788, 279, 744, 462, 561, 358, 666, 495, 504, 345, 679, 247, 778, 643, 379, 495, 504]
	move_all_motors(pos)
	pos = [235, 788, 279, 744, 462, 561, 358, 666, 501, 510, 342, 681, 242, 782, 646, 377, 501, 510]
	move_all_motors(pos)
	pos = [235, 788, 279, 744, 462, 561, 358, 666, 507, 516, 341, 682, 240, 783, 647, 376, 507, 516]
	move_all_motors(pos)

def fall():
	move_motor = rospy.ServiceProxy('move_motor', MoveMotor)

	pos = [210, 814, 292, 732, 484, 540, 355, 669, 508, 515, 512, 512, 520, 504, 512, 512, 500, 524]
	move_all_motors(pos)

	#bowing
	resp1 = move_motor(13, 450, 60)
	resp1 = move_motor(14, 571, 60)
	resp1 = move_motor(15, 577, 60)
	resp1 = move_motor(16, 447, 60)
	resp1 = move_motor(11, 594, 60)
	resp1 = move_motor(12, 430, 60)

	time.sleep(0.2)

	resp1 = move_motor(13, 323, 40)
	resp1 = move_motor(14, 701, 40)
	resp1 = move_motor(15, 660, 40)
	resp1 = move_motor(16, 364, 40)
	resp1 = move_motor(11, 594, 40)
	resp1 = move_motor(12, 430, 40)

	time.sleep(1)

	#hands to protect
	resp1 = move_motor(1, 540, 40)
	resp1 = move_motor(2, 494, 40)
	resp1 = move_motor(3, 213, 40)
	resp1 = move_motor(4, 811, 40)
	resp1 = move_motor(5, 512, 40)
	resp1 = move_motor(6, 512, 40)

	#start falling

	resp1 = move_motor(11, 570, 40)
	resp1 = move_motor(12, 454, 40)

	resp1 = move_motor(11, 550, 40)
	resp1 = move_motor(12, 474, 40)

	resp1 = move_motor(11, 530, 40)
	resp1 = move_motor(12, 494, 40)

	resp1 = move_motor(11, 510, 40)
	resp1 = move_motor(12, 514, 40)

	resp1 = move_motor(11, 490, 40)
	resp1 = move_motor(12, 534, 40)

	resp1 = move_motor(11, 470, 40)
	resp1 = move_motor(12, 554, 40)

	resp1 = move_motor(11, 450, 40)
	resp1 = move_motor(12, 574, 40)

	resp1 = move_motor(11, 430, 40)
	resp1 = move_motor(12, 594, 40)

	resp1 = move_motor(11, 410, 40)
	resp1 = move_motor(12, 614, 40)

	resp1 = move_motor(11, 390, 40)
	resp1 = move_motor(12, 634, 40)


