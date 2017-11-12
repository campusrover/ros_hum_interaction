#!/usr/bin/env python

from espeak import espeak
import rospy
from std_msgs.msg import String

from threading import *
import threading
from multiprocessing import Process



def callback(msg):
	#print threading.activeCount()
	#p = None
	#if 'hi' in msg.data:
		print 'in here'
		p = Thread(target=espeak.synth, args=('hello i am leonardo',))
		p.start()
		p.join()
	#p.terminate()		
	print 'done'	
		#espeak.synth('Hello, I am Leonardo')


rospy.init_node('speech')

sub = rospy.Subscriber('voice', String, callback)

rospy.spin()



