#!/usr/bin/env python3

import rospy
from homework4_1msgs.msg import hw4_pt1

class Homework4:
    def __init__(self):
        rospy.Subscriber("/homework1/total", hw4_pt1, self.callback)
        self.pub = rospy.Publisher("/homework3/converted_total", hw4_pt1, queue_size=10)
        self.unit_holder
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
        
        a_hw4_pt1_message = hw4_pt1()
        a_hw4_pt1_message.unit_holder = "A wonderful number!"
        a_hw4_pt1_message.HW1 = 14
		
		
if __name__ == '__main__':
	rospy.init_node('homework4_1', anonymous=True)
	Homework4()

    # spin() simply keeps python from exiting until this node is stopped
	rospy.spin()
