#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float32
from PIDclass import PID
from duckietown_msgs.msg import Twist2DStamped, LanePose


class lab3:
    def __init__(self):
        global controller1
        global controller2
        
        controller1 = PID(0)
        controller1.setGains(10,0,0)
        
        controller2 = PID(0)
        controller2.setGains(4,0,0)
        
        #if rospy.has_param("/controller_ready"):
        #    rospy.set_param("/controller_ready", 'true')       
    
        rospy.Subscriber("/canard/lane_filter_node/lane_pose", LanePose, self.callback)
        self.pub = rospy.Publisher('/canard/car_cmd_switch_node/cmd', Twist2DStamped, queue_size=10)
        
    
    
    def callback(self, position):
        
        rospy.logwarn("Cody Bellec's lane following program")

        self.output = Twist2DStamped() 
        self.output.v = 0.25
             
        self.angle = -controller1.calc(position.phi) #phi +, angle -
        self.distance = -controller2.calc(position.d-0.07) # d +, angle -
        
        #angle calculation based on distance to center and angle 
        self.output.omega = self.angle + self.distance
        
         
        if self.output.omega >8:
            self.output.omega = 8

        if self.output.omega < -8:
            self.output.omega = -8


        #angle calculation based on distance to center and angle 
        self.output.omega = self.angle + self.distance
        
        self.pub.publish(self.output)
      
           
    
if __name__ == '__main__':
    rospy.init_node('Lane_Followlab3', anonymous=True)
    lab3()
    rospy.spin()
