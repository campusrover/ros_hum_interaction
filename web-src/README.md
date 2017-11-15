## Purpose
The purpose of this README is to document a more complete, web based implementation of the features that have been described in the src/README and the homepage README.

After running into challenges on the TTS and STT side, we decided to make a web server that would run on the TB3, instead of trudging through ROS and pyttsx problems. Ultimately, this implementation will allow a client to handle voice syntehsis, such as a phone or laptop. This way, the TB3 does not have to handle ROS in addition to the computationally expensive TTS and STT modules that we tried.

## Implementation

In order to put a web server on the TB3, we needed to be aware of its hardware limitations as well as our recent exposure to web server design.
The two main choices were REST and RPC, with REST having a much lower barrier to entry and more modules in Python. In terms of ease of use, we found that Flask (https://flask-restful.readthedocs.io/en/latest/quickstart.html) would let us build a RESTful API in the shortest amount of time.

Flask allowed us to construct an API with various endpoints for both JSON requests and HTML requests. The HTML requests were all GETs, in order to access the API through the browser, while the JSON requests were GETs and PUTs. This added some ambiguity to the HTML cases that we had to handle in order to maintain state when no arguments were passed.

Serving up HTML responses were easier than anticipated, thanks to Flask's use of Jinja2 templates (http://jinja.pocoo.org/docs/2.10/templates/), which allowed us to build simple HTML files and then pass appropriate variable values depending on the request we received and the response we wanted to give.

This was done using Flask's ***render_template*** and ***make_response*** methods, which produced a completed template and submitted the HTML back to user, respectively.

One important note is that ROS and Flask cannot both be run in the main thread of execution. You can only run one or the other, with the one being initialized second just hanging. This can be solved by running ROS in the main thread of execution and starting Flask in a daemon thread. Therefore, once the TB3 shutsdown and ROS shutsdow, Flask is terminated automatically. When starting the Flask thread, it is necessary to add a *host* : *TB3_IP* mapping to the **kwargs** dictionary. This allows clients to connect to the web server successfully.

## Features

Each endpoint is handled by a class that implements the appropirate GET. We built four classes that handle different functions for the robot. One class handles GPS data, another handles sounds, another handles status updates, and the final handles basic motor controls. Based upon the arguments sent with particular endpoint, we can make a decision as to how we would like to respond. RESTful argsuments are send as mappings, such as **arg1=val1&arg2=val2.** Flask handles the argument parsing for us, so inside each class we can check for the arguments and their values using **request.args.get(*arg*).** This makes it very easy to determine whether we should stop or go, or play a siren sound or a successful action sound, for example.

## Dependencies

The dependencies for the API can be found at the top of the **api.py** file:

```
from flask import Flask, request, render_template, make_response
from flask_restful import Resource, Api
import rospy
import Queue
from geometry_msgs.msg import Twist
from std_msgs.msg import String
from multiprocessing import Process
from threading import Thread
from playsound import playsound
```
All the python dependencies can be found on the Python 2.7 documentation. To install playsound run `sudo pip install playsound`. Its usage can be seen in **api.py** as well.

## Performance

We envisioned the web server to only serve a single client, such as an Android phone, sitting atop the TB3. In order to server clients concurrently, the challenges of scaling would need to be considered. Having said that, the performace with a single client is quite fast. GETs and PUTs both work quickly and as expected, indicating that HTTP processing can be handled by the Raspberry Pi. One intersting note is that when playing a sound on the TB3, manual adjustment of the volume slider must be done before the sound is played. This is indicative of a threading bug on the Raspberry Pi, and could perhaps be fixed by setting all threads associated with the API as a high priority. This relates back to our overall desire for faster hardware, since our multithreaded approach is bottlenecked by the Raspberry Pi.

## Future Considerations

While the semester may be ending, we hope that the next generation of students will find this code useful and be able to expand on it. These are some additional features that we would have liked to implement but did not have the time to:
* Using a Priority Queue for the Anything to Say endpoint, so messages relating to obstacle avoidance, goal completion, or hardware state will take precedence over messages about location or interaction if such messages happen to arrive concurrently.
* Actually implement a voice synthesizer, perhapns with the help of the CompLing department, so that when the Anything to Say endpoint retrieves a message from the queue, it is able to present as HTML as well as speak it to the user. This would expand into STT as well, allowing an individual to speak a command or phrase, have some ML produce the potential text output and then have that text be PUT onto the web server.
