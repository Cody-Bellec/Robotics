#!/usr/bin/env python3

import sys
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

class ImageProcess:
    def __init__(self):
        # Instatiate the converter class once by using a class member
        self.bridge = CvBridge()
        rospy.Subscriber("/image", Image, self.processing)
        self.pubcrop = rospy.Publisher("/image_cropped", Image, queue_size=10)
        self.pubwhite = rospy.Publisher("/image_white", Image, queue_size=10)
        self.pubyellow = rospy.Publisher("/image_yellow", Image, queue_size=10)
       
    def processing(self, msg):
   
        #cut off top half
        cv_img1 = self.bridge.imgmsg_to_cv2(msg, "bgr8")
        height = cv_img1.shape[0]
        width = cv_img1.shape[1]
        cropped = cv_img1[int(height/2):height, 0:width]
        roscropped = self.bridge.cv2_to_imgmsg(cropped, "bgr8")
        self.pubcrop.publish(roscropped)
        #
       
       
        #
        cv2cropped = cv2.cvtColor(cropped, cv2.COLOR_BGR2HSV)
        white_filtered = cv2.inRange(cv2cropped, (0,0,240),(180,255,255))
        wf = self.bridge.cv2_to_imgmsg(white_filtered, "mono8")
        self.pubwhite.publish(wf)
        #white filtering
        #
       
       
        #
        yellow_filtered = cv2.inRange(cv2cropped, (20, 100, 100),(180,255,255))
        yf = self.bridge.cv2_to_imgmsg(yellow_filtered, "mono8")
        self.pubyellow.publish(yf)
        #yellow filtering
        #

if __name__=="__main__":
    # initialize our node and create a publisher as normal
    rospy.init_node("homework8.py", anonymous=True)
    img_flip = ImageProcess()
    rospy.spin()
