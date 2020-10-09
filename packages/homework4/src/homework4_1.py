#!/usr/bin/env python3

import rospy
from hw4_pt1.msg import HW1

class Homework4:
    def __init__(self):
        rospy.Subscriber("/homework1/total", HW1, self.callback)
        self.pub = rospy.Publisher("/homework3/converted_total", HW1, queue_size=10)
    def callback(self, data):
		
        if rospy.has_param("unit_holder"):
            self.mode = rospy.get_param("unit_holder")
        else:
            self.mode = 'meters'
    			
        if self.mode == 'smoots':
            turnout = data.data * 1.7018
        elif self.mode == 'feet':
            turnout = data.data
        else:
            turnout = data.data * 3.2808
		
            self.pub.publish(turnout)
            rospy.loginfo("input data: %lf feet. output data: %lf %s", data.data, turnout, self.mode)
		
		
if __name__ == '__main__':
	rospy.init_node('homework4_1', anonymous=True)
	Homework4()

    # spin() simply keeps python from exiting until this node is stopped
	rospy.spin()
