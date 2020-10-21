#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float32
from duckietown_msgs.msg import Twist2DStamped

class Circle:
    def __init__(self):
        self.pub = rospy.Publisher("car_cmd_switch_node/cmd", Twist2DStamped, queue_size=10)

    def callback(self, velocity, turnrate):
        velocity = 1.00
        turnrate = 4.5
        
        turnout = Twist2DStamped()
        self.turnout.v = velocity
        self.turnout.omega = turnrate
          
        self.pub.publish(turnout)

if __name__ == '__main__':
    try:
        c = Circle()
        rospy.init_node('circle', anonymous=True)
        c.callback(1.00, 4.5)
        drive = c.callback * 4
        c.callback(0, 0)
        
        
       #rate = rospy.Rate(1) # 1hz
       #while not rospy.is_shutdown():
           #c.callback()
           #rate.sleep()
    except rospy.ROSInterruptException:
        pass
