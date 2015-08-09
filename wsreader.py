###
# wsreader.py
#
# a StackExchange websocket reader to get a live feed of
# every question asked on SE.
###

import websocket
import time
from stackexchange.question import Question


##
# Start connections
##
print("Initializing Ultron connection...")
ws = websocket.create_connection("ws://qa.sockets.stackexchange.com/")
ws.send("155-questions-active")
# Chat connection goes here
print("Connection created.")

while True:
  try:
    a = ws.recv()
    if (a is not None and a != ""):
      q = Question.createFromWebsocket(a)
      print(q.markdownStr())
  except Exception as e:
    print(type(e))
    print(e.args)
    print(e)
