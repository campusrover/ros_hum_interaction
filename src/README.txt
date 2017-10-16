THIS SRC FOLDER CONTAINS THE CODE MEANT FOR THE HUMAN INTERACTION TEAM OF PITO SALAS'S ROBOTICS LAB.

DOCUMENTATION:
(Because pocketsphinx is wrapped for Kinetic and has not been well documented, we have recorded the steps that we took in order to figure out the installation/setup/config.)

Speech to Text requires: pocketsphinx (see https://answers.ros.org/question/246247/speech-recognition-packages-for-ros-kinetic-kame/ for discussion on this, see https://github.com/Pankaj-Baranwal/pocketsphinx/ for implementation of package in Kinetic Kame, see http://www.pirobot.org/blog/0022/ for success but on a different distro)

<TODO: post notes on the steps on how to get it set up. Takes a lot of small and annoying steps.>
POCKETSPHINX STEPS FOR INSTALLATION AND CONFIGURATION:


Text to Speech requires: pyttsx (see https://pyttsx.readthedocs.io/en/latest/ for documentation, also see the Programming with ROS textbook for sample code on this package)
Terminal:
  pip install pyttsx
  
...and you're all set for text to speech!

NOTES:
A good chunk of what we posted here is recognizer.py. This is the fundamental code that runs pocketsphinx! SEE the small changes we made to -lm (because that's what we ended up using instead of -kws as that is an extra parameter that we don't use; only lm and dict is used.)
LOOK AT LINE 61. The direct path for the config is specified, so if you want to run the launch file on your virtual machine then you'll have to specify where your dict file is (our case is 4707).
pyttsx is like any other package. All you have to do is import it in your subscriber node and use it in your callback after listening to messages/strings published by pocketsphinx.
