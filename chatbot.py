###
# chatbot.py
# This script manages the chat interface for ultron
###

import os
import getpass
import sys
import time

import chatexchange3
from wolfram import Wolfram
from globals import Globals

##
# Variables
##
promptStr = '::'
command_description = {
  'whoami'  : 'Lists the user ID for the account running this bot on this site',
  'help'    : 'Displays this help text.',
  'about'   : 'Displays purpose statement/bot greeting.',
  'wolfram' : ('Evaluates a string with the Wolfram Alpha API. '
               '(Note: the account can only make 2000 requests/month, so this '
               'is rate-limited per day. Privileged users can exceed the '
               'rate-limiting.)'),
  'say'     : 'Sends a message with provided text (privileged users only).',
  'star'    : 'Stars the message with provided number (privileged users only)',
  'die'     : 'Kills chatbot (privileged users only)'
  }

##
# Loads config variables, etc, from environment variables or typing
##
def load_config():
  if 'ChatExchangeU' in os.environ:
    Globals.ChatExchangeU = os.environ['ChatExchangeU']
  else:
    Globals.ChatExchangeU = input("Email: ")

  if 'ChatExchangeP' in os.environ:
    Globals.ChatExchangeP = os.environ['ChatExchangeP']
  else:
    Globals.ChatExchangeP = getpass.getpass("Password: ")

  if 'WolframApiKey' in os.environ:
    Globals.WolframApiKey = os.environ['WolframApiKey']
  else:
    Globals.WolframApiKey = input("Wolfram API Key (if none, just press enter): ")

##
# Reply to a given message
##
def reply_to(text, room, source_message):
  room.send_message(':{} {}'.format(source_message.id, text))

##
# Confirm sender is privileged
# If not privileged, reply to message with reason and return true.
# If privileged, return true
##
def check_privilege(client, room, message):
  if (Globals.is_privileged(client, message.owner.id)):
    return True
  reply_to("This command is only accessible to privileged users.", room, message)
  return False

##
# Handle chat commands
# Note: every command should have a "help text" in the command_description
# dictionary
##
def handle_command(command, args, client, room, source_message):
  print("Received command '{}' with args: '{}'.".format(command, args))
  if command == 'whoami':
    me = client.get_me()
    reply_to('My ID for this site is {}.'.format(me.id), room, source_message)
  elif command == 'about':
    help_text = ("Hi! I'm *" + Globals.bot_name + "*, a chatbot designed for Math.SE.  "
                 "I'm still in the developmental stages, but I will eventually detect "
                 "low-quality questions. For a list of my commands, try `::help`.")
    reply_to(help_text, room, source_message)
  elif command == 'say':
    if check_privilege(client, room, source_message):
      room.send_message(args)
  elif command == 'star':
    if check_privilege(client, room, source_message):
      # TODO: check args for errors
      to_star = client.get_message(int(args))
      to_star.star()
      reply_to("Ok.", room, source_message)
  elif command == 'die':
    if check_privilege(client, room, source_message):
      reply_to("Goodbye, cruel world!", room, source_message)
      time.sleep(5) # make sure the message goes through
      sys.exit(0)
  elif command == 'help':
    if not args:
      reply_to(("Send commands by typing `::[command-name]`. I know the "
                "following commands:"), room, source_message)
      response = ""
      for k in command_description:
        response += "     - " + k + "\n"
      room.send_message(response)
      room.send_message("For information about a particular command, try "
                        "typing `help [command-name]`")
    elif args in command_description:
      reply_to(command_description[args], room, source_message)
    else:
      reply_to("I'm sorry, I don't understand with what you need help.",
               room, source_message)
  elif command == 'wolfram':
      reply_to(Globals.wolf.smart_query(args), room, source_message)
  else:
    reply_to("I'm sorry, I don't understand that command.", room, source_message)

##
# Run the chat monitor
##
if __name__ == '__main__':
  ## Startup
  print("Loading configuration...")
  load_config()

  print("Connecting to host...")
  client = chatexchange3.Client(Globals.room_domain['test'], Globals.ChatExchangeU, Globals.ChatExchangeP)
  testroom = client.get_room(Globals.room_id['test'])
  Globals.wolf = Wolfram(Globals.WolframApiKey)

  print("Ready")

  ## Monitor all messages in the room
  for message in testroom.new_messages():
    text = message.content

    if (text.startswith(promptStr)):
      # handle commands
      split_form = text[len(promptStr):].split(' ', 1)
      command = split_form[0]
      args = ''
      if len(split_form) > 1:
        args = split_form[1]
      handle_command(command, args, client, testroom, message)

    print (message.content)
