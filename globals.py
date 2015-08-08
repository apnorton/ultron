##
# Globals
#
#  This file contains information relevant to the entire ultron codebase,
# not just a single file. 
##

import chatexchange3

class Globals:
  
  #### Variables ####

  ## Login information and API keys
  ChatExchangeU = None
  ChatExchangeP = None
  WolframApiKey = None

  ## Chatroom information (k in roomID iff k in roomDomain)
  roomID = {
    'test'   : 911,
    'tavern' : 89
    }

  roomDomain {
    'test'   : 'meta.stackexchange.com',
    'tavern' : 'meta.stackexchange.com'
    }

  #### Functions ####

  def isWolframEnabled():
    return not WolframApiKey

