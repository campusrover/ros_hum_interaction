#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

class Motion:
	def __init__(self):
		self.pub = rospy.Publisher('/robot0/cmd_vel', Twist, queue_size=1)
		self.twist = Twist()

	def turn_left(self, speed=None):
		if speed is not None:
			self.twist.angular.z = speed
			self.pub.publish(self.twist)
		else:
			self.twist.angular.z = .2
			self.pub.publish(self.twist)

	def turn_right(self, speed=None):
		if speed is not None:
			self.twist.angular.z = speed
			self.pub.publish(self.twist)
		else:
			self.twist.angular.z = -.2
			self.pub.publish(self.twist)
	
	def forward(self, speed=None):
		if speed is not None:
			self.twist.linear.x = speed
			self.pub.publish(self.twist)
		else:
			self.twist.linear.x = .2
			self.pub.publish(self.twist)

	def stop(self):
		self.twist.linear.x = 0
		self.twist.angular.z = 0
		self.pub.publish(self.twist)

