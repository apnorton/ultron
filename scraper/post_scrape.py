import re
import csv
import sys
import json
import requests
import traceback
from sys import argv
from time import sleep
from bs4 import BeautifulSoup

cookies = None
base_url =  'http://math.stackexchange.com/q/'

def get_web(url):
  global cookies

  #TODO do some more advanced kind of error checking here
  r = requests.get(url, cookies=cookies)
  if not r.ok:
    print ('Error loading {}'.format(url))

  return r.text

def load_cookies():
  global cookies
  data = None
  with open('cookies.json', 'r') as jfile:
    data = json.load(jfile)
  cookies = data['cookies']

def parse_rep(span_tag):
  if span_tag.get('title') == 'reputation score ': # no k-notation
    rep_string = span_tag.getText().replace(',', '')
  else: # k-notation!
    rep_string = span_tag.get('title')[17:] # 17 = len('reputation score ')

  return int(rep_string)

# lst is a list of span tags of class post-signature
def select_owner(lst):
  for span in lst:
    if 'asked' in span.select('.user-action-time')[0].getText():
      return span

  return None

def parse_page(q_id, html):
  soup = BeautifulSoup(html, 'html.parser')

  vote_count = int(soup.select('.vote-count-post')[0].getText())
  question_title = soup.select('#question-header')[0].getText()
  question_text = soup.select('.post-text')[0].getText()
  question_tags = [x.getText() for x in set(soup.select('.post-tag'))]
  owner = select_owner(soup.select('.post-signature'))
  owner_url = owner.select('.user-details')[0].select('a')[0].get('href')
  owner_id = re.search('/users/(?P<id>\d+)/.*', owner_url).group('id')
  owner_rep = parse_rep(owner.select('.reputation-score')[0])

  data = [
    q_id,
    question_title.strip(),
    question_tags,
    vote_count,
    owner_rep,
    owner_id,
    question_text.strip()
  ]

  return data


if __name__=='__main__':
  # Get the cookies to impersonate my account
  load_cookies()

  start_index = 0
  if len(argv) > 1:
    start_index = int(argv[1])

  print('Starting the scrape at position {} in list.'.format(start_index))

  with open('my_votes.txt', 'r') as f:
    questions = f.read().splitlines()
    for i in range(start_index, len(questions)):
      q = questions[i]
      print('Downloading question {}...'.format(q))
      html = get_web(base_url + q)
      print('Parsing...')
      try:
        row = parse_page(int(q), html)
      except Exception as ex:
        traceback.print_exc()
        print(ex)
        print('The html code that failed to parse has been written to file:')
        with open('err.out', 'w') as err:
          for l in html.splitlines():
            err.write(l)
            err.write('\n')

        sys.exit(1)
      print('Writing...')

      with open('data.csv', 'a') as output:
        writer = csv.writer(output)
        writer.writerow(row)

      print('Done with index {}.'.format(i))
      sleep(5)
