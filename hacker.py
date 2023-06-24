import requests
from bs4 import BeautifulSoup
import pprint

url = requests.get('https://news.ycombinator.com/')
r = url.text
soup_object = BeautifulSoup(r, 'html.parser')
heading = soup_object.select('.titleline > a')
pts = soup_object.select('.subtext')


def sort_hn(hnlist):
	return sorted(hnlist, key = lambda k:k['votes'], reverse = True)


def req_hn(heading,pts):
	news = []
	for i, t in enumerate(heading):
		title = t.getText()
		href = t.get('href', None)
		s = pts[i].select('.score')
		if len(s):
			vote = int(s[0].getText().replace(" points", " "))
			if vote > 99:
				news.append({'title': title, 'links': href, 'votes': vote})
	return sort_hn(news)



pprint.pprint(req_hn(heading,pts)) 
	    
	




