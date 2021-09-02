#! usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String

class RoboticArm():
    def __init__(self):
        
        self.callbackF 

        self.sub = rospy.Subscriber("/serial/robotic_arm", String, self.callbackF)
        self.subF 


    def callbackF(self,msg):
        rospy.loginfo(msg)

    

    def subF(self):
        rospy.init_node("robotic_arm")
        rospy.spin()

obj = RoboticArm()
obj.subF()