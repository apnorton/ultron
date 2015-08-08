##
# chatbot.py
# This script manages the chat interface for ultron
##

import os
import getpass

import chatexchange3

## Standard "get username and password" stuff
if 'ChatExchangeU' in os.environ:
  email = os.environ['ChatExchangeU']
else:
  email = input("Email: ")
if 'ChatExchangeP' in os.environ:
  password = os.environ['ChatExchangeP']
else:
  password = getpass.getpass("Password: ")

## Connect to test room and figure out who I am
print("Connecting to host...")
client = chatexchange3.Client('meta.stackexchange.com', email, password)
testroom = client.get_room(911)
me = client.get_me()
print(me.__dict__)

testroom.send_message("I'm online!")

for message in testroom.new_messages():
  text = message.content
  if (text.startswith("//")):
    # handle commands
    if (text[2:].startswith("whoami")):
      testroom.send_message("My user ID is {}.".format(me.id))
  print (message.content)
