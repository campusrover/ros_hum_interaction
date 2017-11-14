# Alternative Solutions (That Produced the Similar Errors)

The following code has been described in the overall README, but you may find these specific details regarding this code useful:
Note that some of the solutions that we have done do not appear because we either undid everything or deleted the lines of code
upon noticing failure (ex: tried event loops but didn't work either).

###voice.py
This code is just to test pyttsx. Notice that some lines have been removed, with a hidden trace of the callback being commented
out. This is because in the callback we tried multi-threading, then we resorted to an even simpler example of Leonardo just
uttering a string.
####Important Takeaways:
What does runAndWait() actually do? What's being blocked, also think about this in a Raspberry Pi processor point of view.
See https://pyttsx.readthedocs.io/en/latest/ for more info.

###responder.py && dummy.py
This code is to test services in ROS using our never ending callback. Why did we do this? Because we had assumed that a 
publisher/subscriber mechanism must have been weak by itself, unable to handle our infinite msg and parsing. Notice on the top 
that we use the Chapter19 server to send our messages and wait for a result. The server is handling things a different way
so that a subscriber's callback doesn't have to do it.
####Important Takeaways:
Read Chapter 19! It's useful to understanding services and getting a robot to speak. Also, consider this question:
Do we have enough power to run pyttsx in a callback? Consider Pito's resource, Rodney A. Brooks "A Robut Layered Control System
For A Mobile Robot". Take note that a robot requires additivity, in which a robot eventually needs more processing power.
Should we spend more time utilizing our excess power, upgrading it, or stacking more processors in the architecture? (I think the
last point is the way to go.)

###speech.py
This code is to test multithreading and espeak. We tried using festive but it's been deleted in our code (you can still use it
on Leonardo since it's already installed). The commented out things are for the purpose of debugging.
####Important Takeaways:
How well do we understand threading that it may be used effectively in ROS? Do we need it?
