#!/usr/bin/env python

# Copyright (C) 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from __future__ import print_function

import argparse
import os.path
import json
import rospy
from motion import Motion
import google.oauth2.credentials

from google.assistant.library.assistant import Assistant
from google.assistant.library.event import EventType
from google.assistant.library.file_helpers import existing_file


def process_event(event):
    if(event.type == EventType.ON_RECOGNIZING_SPEECH_FINISHED):
		if 'turn left' in event.args[u'text']:
			move = Motion()
			move.turn_left()
			del move
		if 'turn right' in event.args[u'text']:
			move = Motion()
			move.turn_right()
			del move
		if 'forward' in event.args[u'text']:
			move = Motion()
			move.forward()
			del move
		if 'end motion' in event.args[u'text']:
			move = Motion()
			move.stop()
			del move
	
    else:
		print (event)

def main():
    rospy.init_node('voice')
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('--credentials', type=existing_file,
                        metavar='OAUTH2_CREDENTIALS_FILE',
                        default=os.path.join(
                            os.path.expanduser('~/.config'),
                            'google-oauthlib-tool',
                            'credentials.json'
                        ),
                        help='Path to store and read OAuth2 credentials')
    args = parser.parse_args()
    with open(args.credentials, 'r') as f:
        credentials = google.oauth2.credentials.Credentials(token=None,
                                                            **json.load(f))

    with Assistant(credentials) as assistant:
        for event in assistant.start():
            process_event(event)
	    if event.type == EventType.ON_CONVERSATION_TURN_FINISHED and event.args['with_follow_on_turn']==False:
		assistant.start_conversation()


if __name__ == '__main__':
    main()
