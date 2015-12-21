import re
import json
import requests
from bs4 import BeautifulSoup

cookies = None
base_url =  'http://math.stackexchange.com/users/23353/apnorton?tab=votes'
vote_type = 'closure'

def get_web(url):
  global cookies

  #TODO do some more advanced kind of error checking here
  r = requests.get(url, cookies=cookies)
  if not r.ok:
    print ('Error')

  return r.text

def load_cookies():
  global cookies
  data = None
  with open('cookies.json', 'r') as jfile:
    data = json.load(jfile)
  cookies = data['cookies']

def get_questions(html):
  soup = BeautifulSoup(html, 'html.parser')
  anchors = soup.select('.question-hyperlink')

  # Apply a filter to just get the number of each question
  qs = []
  for a in anchors:
    url = a.get('href') # just the question url
    q_num = re.search('/(?P<num>\d+)/.*', url).group('num')
    qs.append(q_num)

  return qs

if __name__=='__main__':
  # Get the cookies to impersonate my account
  load_cookies()

  # Set up URL
  url = base_url + '&sort=' + vote_type + '&page='
  questions = []
  for i in range(1, 85):
    html = get_web(url+str(i))
    questions += get_questions(html)

  print('Parsed 85 pages, loaded {} questions.'.format(len(questions)))

  with open('my_votes.txt', 'w') as outfile:
    for q in questions:
      outfile.write(q)
      outfile.write('\n')
