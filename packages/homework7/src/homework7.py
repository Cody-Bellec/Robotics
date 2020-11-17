#!/usr/bin/env python3

import rospy
import math
from std_msgs.msg import Float32
from odometry_hw import DistWheel, Pose2D

class HW7:
    def __init__(self):
        rospy.Subscriber("/dist_wheel", DistWheel, self.callback)
        self.pub = rospy.Publisher('/pose', Pose2D, queue_size=10)
        
        global Pose
        Pose = Pose2D()
        Pose.x = 0
        Pose.y = 0
        Pose.theta = 0
    def callback(self,wheel):
        Delta_sL = wheel.dist_wheel_left
        Delta_sR = wheel.dist_wheel_right
        
        L = 0.05
        
        Delta_s = (Delta_sL + Delta_sR)/2
        Delta_theta = (Delta_sR - Delta_sL)/(2*L)
        Delta_x = Delta_s * cos(Pose.theta + (Delta_theta/2))
        Delta_y = Delta_s * sin(Pose.theta + (Delta_theta/2))
        Pose.x = Pose.x + Delta_x
        Pose.y = Pose.y + Delta_y
        Pose.theta = Pose.theta + Delta_theta
        
        self.pub.publish(Pose)
        
if __name__ == '__main__':
    rospy.init_node('homework7.py', anonymous = True)
    HW7()
    rospy.spin()
        
       
