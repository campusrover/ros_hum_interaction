#! /usr/bin/env python

import rospy
from std_msgs.msg import String

rospy.init_node('dummy')
pub = rospy.Publisher('voice', String, queue_size=1)
rate = rospy.Rate(100)
while not rospy.is_shutdown():
	pub.publish('hi')
	rate.sleep()
