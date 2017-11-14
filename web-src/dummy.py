#!/usr/bin/env python
import rospy
from std_msgs.msg import String

rospy.init_node('dummy_tell')
dummy_tell_pub = rospy.Publisher('dummySay', String, queue_size = 1)

rate = rospy.Rate(0.1)
while not rospy.is_shutdown():
	msg = 'Hi, I am Michel-I mean Leonardo.'
	print 'output: ' + msg
	dummy_tell_pub.publish(msg)
	rate.sleep()
