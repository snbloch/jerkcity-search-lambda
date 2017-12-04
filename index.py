from pyquery import PyQuery as pq
from random import randint
import urllib

def jerksearch(event, context):
    url = 'https://www.jerkcity.com/search/?'
    quotes = []
    if event.get('q') is None and len(event.get('text')) != 0:
        event['q'] = event.pop('text')
    querystring = urllib.urlencode(event)
    url = url + querystring
    page = pq(url=url)
    quotes = [i.text() for i in page.items('.dialog')]
    if len(quotes) > 0:
        random_quote = quotes[randint(0, len(quotes) - 1)]
        return random_quote
    else:
        return 'No result found for query ' + event['q']
