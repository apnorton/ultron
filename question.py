class Question:
  ##
  # Question(wsResponse):
  # This initializer forms the current question with
  # a bunch of empty fields
  ##
  def __init__(self):
    self.sitename = None
    self.title = None
    self.qid = None
    self.url = None
    self.asker = None
    self.askerUrl = None
    self.askerID = None
    self.tags = None
    self.time = None
    self.body = None

  def createFromWebsocket(wsResponse):
    data = eval(eval(wsResponse)['data']) # converts nested dictionary to string
    q = Question() 
    q.sitename = data['apiSiteParameter']
    q.title = data['titleEncodedFancy']
    q.qid = int(data['id'])
    q.url = data['url']
    q.asker = data['ownerDisplayName']
    q.askerUrl = data['ownerUrl']
    q.askerID = None # Need to parse from data['ownerUrl']
    q.tags = data['tags']
    q.time = int(data['lastActivityDate'])
    q.body = None
    return q

  def retrieveBody(self):
    # Do something with either an API call or a direct visit to the webpage.
    return

  def markdownStr(self):
    return "[{}]({}) asked by [{}]({})".format(self.title, self.url, self.asker, self.askerUrl)
