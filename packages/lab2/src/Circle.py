#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float32
from duckietown_msgs.msg import Twist2DStamped

class Circle:
    def __init__(self):
        self.pub = rospy.Publisher("/canard/car_cmd_switch_node/cmd", Twist2DStamped, queue_size=10)

    def callback(self, velocity, turnrate):
        
        turnout = Twist2DStamped()
        self.turnout.v = velocity
        self.turnout.omega = turnrate
          
        self.pub.publish(self.turnout)

if __name__ == '__main__':
    try:
        c = Circle()
        rospy.init_node('circle', anonymous=True)
        c.callback(1.0, 4.5)
        c.callback(1.0, 4.5)
        c.callback(1.0, 4.5)
        c.callback(1.0, 4.5)
        rospy.sleep(7)
        c.callback(0, 0)
        
    except rospy.ROSInterruptException:
        pass
