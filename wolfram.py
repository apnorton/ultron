###
# Wolfram
# This class is to be used in connection with the Wolfram Alpha API.
###

import xmltodict
import urllib.request
import urllib.parse

class Wolfram:
  api_url ='http://api.wolframalpha.com/v2/query?'
  def __init__(self, api_key=''):
    if not api_key:
      self.api_key = None
    else:
      self.api_key = api_key

  def smart_query(self, text):
    response = self.make_request(text)['queryresult']
    print(response, "\n")
    # Check if request failed:
    if response['@success'] == 'false':
      if response['@error'] == 'true':
        return "Request failed with message: " + response['error']['msg']
      else:
        return "Request failed with no error message."

    primary_pod= None
    for pod in response['pod']:
      if '@primary' in pod and pod['@primary'] == 'true':
        primary_pod = pod

    # In the future, handle requests without primary pods... but not yet.
    if not primary_pod:
      return "Request succeeded, but no primary pod existed; unknown response."

    if '@numsubpods' in primary_pod and primary_pod['@numsubpods'] == '1':
      subpod = primary_pod['subpod']
      # If they've managed to give us plaintext, we want it.
      # TODO use https://github.com/jgm/texmath to convert MathML to TeX
      if 'plaintext' in subpod:
        return subpod['plaintext']
      else: # return the image
        return subpod['img']['@src']

    else:
      return "Unknown number of subpods in response."

    # TODO make a request, decide what to do with it, then return proper data
    return "Something bad happened"

  def make_request(self, text):
    params = {
      'appid' : self.api_key,
      'input' : text
      }
    url_params = urllib.parse.urlencode(params)
    url = Wolfram.api_url + url_params
    print(url)
    dict_form = None
    with urllib.request.urlopen(url) as response:
      dict_form = xmltodict.parse(response)
    return dict_form
