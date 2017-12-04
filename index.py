from pyquery import PyQuery as pq
from random import randint
import urllib

def jerksearch(event, context):
    url = 'https://www.jerkcity.com/search/?'
    quotes = set([])
    if event.get('q') is None and len(event.get('text')) != 0:
        event['q'] = event.pop('text')
    querystring = urllib.urlencode(event)
    url = url + querystring
    page = pq(url=url)
    for i in page.items('a'):
        if '.html' in i.attr['href']:
            quotes.add(i.attr['href'])
    if len(quotes) > 0:
        quotes = list(quotes)
        random_quote = quotes[randint(0, len(quotes) - 1)]
        url = 'http://www.jerkcity.com' + random_quote
        page = pq(url=url)
        for i in page.items('.aidsy'):
            image = i.attr['src']
            return 'http://www.jerkcity.com' + image
    else:
        return 'No result found for query ' + event['q']
