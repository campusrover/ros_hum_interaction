#!/usr/bin/env python

import rospy
import pyttsx
from std_msgs.msg import String
from threading import Thread




	#global engine
while True:

	engine = pyttsx.init()	
	engine.say('Hello, I am Leonardo')
	engine.runAndWait()
	#sub = rospy.Subscriber('voice', String, voice_callback)




