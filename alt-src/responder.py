#! /usr/bin/env python

import actionlib
from chapter19.msg import TalkAction, TalkGoal
import rospy
from std_msgs.msg import String

rospy.init_node('responder')
client = actionlib.SimpleActionClient('speak', TalkAction)
client.wait_for_server()

def voice_callback(msg):
	goal = TalkGoal()
	if 'hi' in msg.data:
		goal.sentence = "hi, I am Leonardo"
		client.send_goal(goal)
		client.wait_for_result()

sub = rospy.Subscriber('voice', String, voice_callback)
rospy.spin()
