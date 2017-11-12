# Repository Notes / HOW TO USE:

This repository may be used as a ROS package with regards to our initial project:
  "Getting a TurtleBot3 to speak without using a Cloud Service"
  Note that if you want to use that portion of the project, you only need the 'src' folder, CMakeLists.txt,
  and package.xml. See README in src folder for more instructions on how to get this set up.
  
  Our alternative solution uses the 'templates' folder and 'api.py', in which you must create a separate package
  to test this out in ROS. 'templates' has to be in the same directory as api.py so that'll probably mean
  you put it in your src folder of your new package.
  
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
