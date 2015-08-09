##
# Globals
#
#  This file contains information relevant to the entire ultron codebase,
# not just a single file.
##

import chatexchange3

class Globals:
  #### Variables ####

  ## About me
  bot_name = 'A Familiar Face'

  ## Login information and API keys
  ChatExchangeU = None
  ChatExchangeP = None
  WolframApiKey = None

  ## Chatroom information (k in roomID iff k in roomDomain)
  room_id = {
    'test'   : 911,
    'tavern' : 89
    }

  room_domain = {
    'test'   : 'meta.stackexchange.com',
    'tavern' : 'meta.stackexchange.com'
    }

  ## Privileged users on a given site
  privileged_users = {
    'meta.stackexchange.com' : [
        201314 # apnorton
      ]
    }

  ## Wolfram client instance
  wolf = None

  #### Functions ####

  def is_wolfram_enabled():
    return not Globals.WolframApiKey

  def is_privileged(client, user):
    return user in Globals.privileged_users[client.host]
