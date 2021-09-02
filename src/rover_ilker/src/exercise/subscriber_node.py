#! usr/bin/env python

import rospy
from std_msgs.msg import String


class subNode():
    def __init__(self):
        self.callback_func
        self.sub = rospy.Subscriber("myTopic", String, self.callback_func)
        self.sub_func

    def callback_func(self,msg):
        rospy.loginfo("data received: " + str(msg))

    def sub_func(self):
        rospy.init_node("sub_node")

        rospy.spin()

obj = subNode()
obj.sub_func()