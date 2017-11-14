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
<TODO>
