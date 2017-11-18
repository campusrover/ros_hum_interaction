# Human Interaction on the TurtleBot3 Using Voice Recognition
*Note: Project runs on ROS Kinetic on VirtualBox/VMWare Ubuntu 16.04

## PURPOSE:
This src folder contains code, testing code, basic examples, and project code meant for the human interface of the Brandeis Campus Rover project.

## DOCUMENTATION:
Because pocketsphinx is wrapped for Kinetic and has not been well documented, we have recorded the steps that we took in order to figure out the installation/setup/config.

This README.txt is supposed to be detailed so that future users of Kinetic Kame and voice recognition can use this as a guide to set it up properly on their machine.


## RESOURCES:
Carnegie Mellon University's Decoder Tools:
http://www.speech.cs.cmu.edu/tools/lmtool-new.html (generate language modeling files)
http://www.speech.cs.cmu.edu/tools/lextool.html (generate pronunciations only)


Speech to Text requires: pocketsphinx (see https://answers.ros.org/question/246247/speech-recognition-packages-for-ros-kinetic-kame/ for discussion on this, see https://github.com/Pankaj-Baranwal/pocketsphinx/ for implementation of package in Kinetic Kame, see http://www.pirobot.org/blog/0022/ for success but on a different distro)

************POCKETSPHINX STEPS FOR INSTALLATION AND CONFIGURATION****************
1. For ROS Kinetic, you need to use this wrapper https://github.com/UTNuclearRoboticsPublic/pocketsphinx
2. Follow the first 2 steps on the README.
3. Step 3 you have to be really careful on:
  3.1 First, locate where your pocketsphinx package has been downloaded to (mine was in the /usr/.../Python2.7 kind of folder, you
  can look it up on your Linux search bar and see where exactly it is.
  3.2 Next interesting thing...you need to sudo everything in your terminal from this point, because there is restricted access.
  3.3 In the pocketsphinx folder, add a "hmm" directory and change the name of the "en-us" directory to "en_US". 
  3.4 Copy the pocketsphinx package into /usr/share, theoretically you just need your model folder.
  Remember if you're having trouble you need to sudo everything to bypass restricted permissions, don't do it on GUI.
  YOU NEED TO HAVE THE EXACT PATH FOR THIS TO WORK.
  
4. If you made it this far, sweet. Do step 4.
5. You have two changes left before things actually work. In recognizer.py of your catkin package, change the keywords file to a language model file and get rid of the associated kw file code. You should have sample code either given / you generated it on the CMU resource. Somewhere in the recognizer.py file you need to put your -lm file parameter. This also assumes that you have put your language model file in the catkin_ws already. (Also put the associated dict file in your dict directory)
6. Lastly, go to your pocketsphinx.launch file. Get rid of the kw lines. In your -lm line, you need to put the direct path of your dict file.

That's it, you're done and hopefully it works. The steps above are so small and specific but it may not work if you don't set it up correctly.


Text to Speech requires: pyttsx (see https://pyttsx.readthedocs.io/en/latest/ for documentation, also see the Programming with ROS textbook for sample code on this package)
Terminal:
  pip install pyttsx
  
(You need to have pip already installed as well, for specifically Ubuntu 16.04 type into your terminal:
  sudo apt-get update && sudo apt-get -y upgrade
  sudo apt-get install python-pip
)

...and you're all set for text to speech!

NOTES ON INSTALLATION / CONFIGURATION:
A good chunk of what we posted here is recognizer.py. This is the fundamental code that runs pocketsphinx! SEE the small changes we made to -lm (because that's what we ended up using instead of -kws as that is an extra parameter that we don't use; only lm and dict is used.)
LOOK AT LINE 61. The direct path for the config is specified, so if you want to run the launch file on your virtual machine then you'll have to specify where your lm file is (our case is 4707).
pyttsx is like any other package. All you have to do is import it in your subscriber node and use it in your callback after listening to messages/strings published by pocketsphinx.


## Launching/Running Nodes and Publishing to the Topic:
Change roslaunch launch file in launch subfolder to only include _dict arg, pointing it to where the .dic file is as generated from the above site. The other arguments will be refernce from inside the recognizer.py file itself.

Individual words will be published to the 'voice' topic, as specified in recognizer.py. This can be changed to any topic that you would like, and you just have to change to subscribers to that topic.

To launch everything as a ROS node, just run roslaunch *name_of_ROS_package* *name_of_launch_file*. This will start the publishing of pocketsphinx data onto the specified topic, which you can subscribe to. An example of this is in voice.py, which sets up a subscriber to the voice node and has a callback which calls the pyttsx runAndWait() method to respond. __Important Note: This method of feeding data from pocketsphinx into a ROS callback does not work on the Raspberry Pi. This is due to a threading issue with the pyttsx runAndWait() method.__


## Problems Relating to Raspberry Pi and TB3.
Since we were running our code on a Turtlebot 3, which is equipped with a Raspberry Pi, we ran into the issue of inadequate hardware. In order to save yourself a headache, take note that this solution does not work at all on the hardware described, and none of our workarounds produced viable results.
These included:
1. Python multiprocessing.
2. Python multithreading.
3. Using an alternative TTS module, such as espeak or festival.

For the future, it would be useful to consider a more powerful SOC, perhaps one made by UDOO, which uses x86 architecture instead the ARM architecture used by the Pi. 
