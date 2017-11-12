#!/usr/bin/env python 

from flask import Flask, request, render_template, make_response
from flask_restful import Resource, Api
import rospy
import Queue
from geometry_msgs.msg import Twist
from std_msgs.msg import String
from multiprocessing import Process
from threading import Thread


app = Flask(__name__)
api = Api(app)
msg_queue = Queue.Queue()
location = {}


def dummyCallback(msg):
	msg_queue.put(msg.data)

sub = rospy.Subscriber('dummySay', String, dummyCallback)
cmd_vel = rospy.Publisher('cmd_vel', Twist, queue_size=1)

class ats(Resource):
	def get(self):
		if not msg_queue.empty():
			return {'speech' : msg_queue.get()}
		else:
			return {'speech' : 'Nothing to say'}

class atsHTML(Resource):
	def get(self):
		if not msg_queue.empty():
			#headers = {'Content Type' : 'text/html'}
			return make_response(render_template('status.html', status=msg_queue.get()))
		else:
			#headers = {'Content-Type': 'text/html'}
			return make_response(render_template('status.html', status='Nothing to Report, Captain'))

class location(Resource):
	def get(self):
		print(request.form['data'])

class locationHTML(Resource):
	def get(self):
		if request.args.get('lat') is not None and request.args.get('long') is not None:
			global location
			location = request.args
			return make_response(render_template('location.html', lat=request.args.get('lat'), lon=request.args.get('long')))
		else:
			return make_response(render_template('location.html', lat=location['lat'], lon=location['long']))

class cmd(Resource):
	def put(self):
		if request.form['data'] == 'stop':
			cmd_vel.publish(Twist())

class cmdHTML(Resource):
	def get(self):
		if request.args.get('cmd') == 'stop':
			cmd_vel.publish(Twist())
			return make_response(render_template('cmd.html'))

api.add_resource(ats, '/ats')
api.add_resource(location, '/location')
api.add_resource(cmd, '/cmd')
api.add_resource(atsHTML, '/robot/ats')
api.add_resource(locationHTML, '/robot/location')
api.add_resource(cmdHTML, '/robot/cmd')

if __name__ == '__main__':
	#app.run(debug=True)
	#change host ip when you want to use on different device
	t = Thread(target=app.run, kwargs={'host' : '129.64.153.118'})
	t.daemon = True
	#t.start() runs flask as its own thread
	t.start()
	rospy.init_node('talker')
	rospy.spin()



