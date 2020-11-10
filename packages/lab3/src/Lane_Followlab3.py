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
        controller1.changeGainz(10,0,0)
        
        controller2 = PID(0)
        controller2.changeGainz(4,0,0)
        
        
    
        rospy.Subscriber("/canard/lane_filter_node/lane_pose", LanePose, self.callback)
        self.pub = rospy.Publisher('/canard/car_cmd_switch_node/cmd', Twist2DStamped, queue_size=10)
        
    
    
    def callback(self, position):
        
        rospy.logwarn("Cody Bellec's lane following program")

        self.output = Twist2DStamped() 
        self.output.v = 0.25
             
        self.angle = -controller1.calc(position.phi) 
        self.distance = -controller2.calc(position.d-0.07) 
        
        
        self.output.omega = self.angle + self.distance
        
         
        if self.output.omega >8:
            self.output.omega = 8

        if self.output.omega < -8:
            self.output.omega = -8


        
        self.output.omega = self.angle + self.distance
        
        self.pub.publish(self.output)
      
           
    
if __name__ == '__main__':
    rospy.init_node('Lane_Followlab3', anonymous=True)
    lab3()
    rospy.spin()
