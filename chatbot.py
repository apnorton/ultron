##
# chatbot.py
# This script manages the chat interface for ultron
##

import os
import getpass
import chatexchange3
from globals import Globals

##
# Variables
##
promptStr = ':>'

##
# Loads config variables, etc, from environment variables or typing
##
def loadConfig():
  if 'ChatExchangeU' in os.environ:
    Globals.ChatExchangeU = os.environ['ChatExchangeU']
  else:
    Globals.ChatExchangeU = input("Email: ")

  if 'ChatExchangeP' in os.environ:
    Globals.ChatExchangeP = os.environ['ChatExchangeP']
  else:
    Globals.ChatExchangeP = getpass.getpass("Password: ")

  if 'WolframApiKey' in os.environ:
    Globlas.WolframApiKey = os.environ['WolframApiKey']
  else:
    Globals.WolframApiKey = input("Wolfram API Key (if none, just press enter): ") 

if __name__ == '__main__':
  ## Startup
  print("Loading configuration...")
  loadConfig()

  print("Connecting to host...")
  client = chatexchange3.Client('meta.stackexchange.com', email, password)
  testroom = client.get_room(roomID['test'])

  print("Retreiving room information")
  me = client.get_me()

  print("Ready")

  ## Load basic
  for message in testroom.new_messages():
    text = message.content
    if (text.startswith(promptStr)):
      # handle commands
      (command, args) = tuple(text[len(promptStr)].split(' ', 1))
      if (text[len(promptStr):].startswith("whoami")):
        testroom.send_message("My user ID is {}.".format(me.id))
    print (message.content)
