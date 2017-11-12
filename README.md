# Repository Notes / HOW TO USE:

This repository may be used as a ROS package with regards to our initial project:
  "Getting a TurtleBot3 to speak without using a Cloud Service"
  Note that if you want to use that portion of the project, you only need the 'src' folder, CMakeLists.txt,
  and package.xml. See README in src folder for more instructions on how to get this set up.
  
  Our first alternative solution explores the same Pocketsphinx and Pyttsx issues but with different ways of
  setting up a connection. 
  - We first tried multithreading and debugging by seeing how many active threads are there,
    but that did not work. See documentation on Python threading to understand more.
  - Then, we tried testing espeak with threading (because voice.py tests engine.runAndWait() and we thought that
    that might've been the main issue). espeak didn't work. 
  - Somewhere in the midst of this we tried festival which is an older text to speech synth. It failed a lot more
    than what we did with pyttsx.
  - Finally we tried an Action Server Client, using the example from Programming Robots with ROS. See chapter 19,
    where it says Making Your Robots Talk. We formatted a client for this code, which is responder.py. Note: for
    those of you using ROS Kinetic, use the Chapter19 catkin package here:
      https://github.com/gbiggs/ros_book_sample_code
    The result that we got was that it would respond to us a few times and then it would lag out. 5 minutes later
    it would suddenly spout out all of the responses it should've said beforehand.
  - dummy.py is just to publish strings onto responder.py so that we don't have to say hi all the time (or deal
    with some faultiness of pocketsphinx.
  - (FOR next generation Human Interaction Teams): Refer to my Google Docs Lab Notebook (Jonas Tjahjadi) to see
    exactly all the steps that we have taken.
    
  To reuse any of the alt-src code, create a new package with rospy and std_msgs dependencies, and drag all of the
  code to the src folder of your package.
  
  All of this has concluded that we need more powerful hardware.
  Outside dependencies needed: pyttsx, pocketsphinx
  
  Our second alternative solution uses the 'templates' folder and 'api.py', in which you must create a separate package
  to test this out in ROS. 'templates' has to be in the same directory as api.py so that'll probably mean
  you put it in your src folder of your new package.
  Outside dependencies needed: Flask, RESTful for Flask
Topics of Implementation Include:
  1. ROS Kinetic
  2. Pocketsphinx Speech-to-Text
  3. Pyttsx Text-to-Speech
  4. CMU language models, dictionaries
  5. Basic ROS fundamentals, service, action, pub-sub
  6. (Alternative Solution since above had hardware threading issues):
      Flask with Python and ROS
  
Hardware Needed:
  1. Webcam
  2. Speakers
  3. Keyboard
  4. Of course, a TurtleBot3
  5. HDMI, we used monitor's speakers to get output after receiving from webcam
