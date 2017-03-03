# simplepushbullet.py
A simple library to push notes to devices on pushbullet.

To use copy script to your pythonpath and use

import simplepushbullet.py

send_message(title, message, api_key):

Takes a title, message, and your api key pushes to all devices

send_list(title, message, api_key, divider):

Takes a title, message, api key and character to divide the string up with newline causes Pushbullet to reject it looking into why, Pushes to all devices
