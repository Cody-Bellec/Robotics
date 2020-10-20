#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float32
from duckietown_msgs.msg import Twist2DStamped

class Homework3:
    def __init__(self):
        self.pub = rospy.Publisher("/car_cmd_switch_node/cmd", Twist2DStamped, queue_size=10)

    def callback(self, data):
        velocity = 1.00
        turnrate = 4.5
        
        turnout = Twist2DStamped
        message.v = velocity
        message.omega = turnrate
          
        self.pub.publish(turnout)

if __name__ == '__main__':
    rospy.init_node('homework3', anonymous=True)
    Homework3()
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()
