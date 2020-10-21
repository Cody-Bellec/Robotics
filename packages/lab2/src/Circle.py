#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float32
from duckietown_msgs.msg import Twist2DStamped

class Homework3:
    def __init__(self):
        self.pub = rospy.Publisher("car_cmd_switch_node/cmd", Twist2DStamped, queue_size=10)

    def callback(self):
        velocity = 1.00
        turnrate = 4.5
        
        turnout = Twist2DStamped()
        self.turnout.v = velocity
        self.turnout.omega = turnrate
          
        self.pub.publish(turnout)

if __name__ == '__main__':
    t = Talker()
        rospy.init_node('talker', anonymous=True)
        rate = rospy.Rate(1) # 1hz
        while not rospy.is_shutdown():
            t.talk()
            rate.sleep()
    except rospy.ROSInterruptException:
        pass
