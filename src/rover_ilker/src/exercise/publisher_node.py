#!usr/bin/env python
import rospy
from std_msgs.msg import String

class PublishClass():
	
	def __init__(self):
		self.pub = rospy.Publisher("myTopic", String,queue_size=10)
		self.count = 1
		
	def publisherFunc(self):
		rospy.init_node("pub_node")
		rate = rospy.Rate(1.5)

		rospy.loginfo("publisher node has been initialized")
		while not rospy.is_shutdown():
			msg = String()
			msg.data = "data" + str(self.count)
			rospy.loginfo("data sent")

			self.pub.publish(msg)
			self.count +=1
			rate.sleep()

	
if __name__ == "__main__":
	publishing = PublishClass()
	publishing.publisherFunc()