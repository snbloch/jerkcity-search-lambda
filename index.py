from pyquery import PyQuery as pq
from random import randint
import urllib

def jerksearch(event, context):
    url = 'https://www.bonequest.com/search/?'
    quotes = set([])
    if event.get('q') is None and len(event.get('text')) != 0:
        event['q'] = event.pop('text')
    querystring = urllib.parse.urlencode(event)
    url = url + querystring
    page = pq(url=url)
    for i in page.items('img'):
        if '.gif' in i.attr['src']:
            quotes.add(i.attr['src'])
    if len(quotes) > 0:
        quotes = list(quotes)
        random_quote = quotes[randint(0, len(quotes) - 1)]
        return 'http://www.bonequest.com' + random_quote        
    else:
        return 'No result found for query ' + event['q']
