#!/usr/bin/env python

import rospy
import pyttsx
from std_msgs.msg import String


def voice_callback(msg):
	engine = pyttsx.init()
	if 'hi' in msg.data:
		engine.say('Hello, I am Leonardo')
		engine.runAndWait()
	

def main():
	rospy.init_node('voice')
	sub = rospy.Subscriber('voice', String, voice_callback)
	rospy.spin()

if __name__ == '__main__':
	main()


	




