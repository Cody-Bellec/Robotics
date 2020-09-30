#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float32

class Homework3:
	def __init__(self):
		rospy.Subscriber("/homework1/total", Float32, self.callback)
		self.pub = rospy.Publisher("/homework3/homework3", Float32, queue_size=10)
		self.total = 0

	def callback(self, data):
		self.total += data.data
		self.pub.publish(self.total)
		d_mtrs = int(input("Input distance in meters:"))
		d_mtrs = d_mtrs
		d_ft = d_mtrs * 3.2808
		d_smoot = d_mtrs * 1.7018
		print("The distance in meters is %i meters." % d_mtrs)
		print("The distance in feet is %.2f feet." % d_ft)
		print("The distance in smoots is %.2f smoots." % d_smoot)
	
if __name__ == '__main__':
	rospy.init_node('homework3')
	Homework3()

    # spin() simply keeps python from exiting until this node is stopped
	rospy.spin()
