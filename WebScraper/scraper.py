import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get("https://news.ycombinator.com/")

soup = BeautifulSoup(res.text,"html.parser")
links = (soup.select('.storylink'))
subtext = soup.select('.subtext')
more = soup.select('.morelink')
more_link = more[0].get('href')
print(more_link)
res2 = requests.get("https://news.ycombinator.com/"+more_link)
soup2 = BeautifulSoup(res2.text,"html.parser")
links2 = (soup2.select('.storylink'))
subtext2 = soup2.select('.subtext')

mega_links = links + links2
mega_subtext = subtext + subtext2


def sort_byvotes(hn_list):
	return sorted(hn_list,key=lambda k: k['votes'],reverse=True)

def custom_hn(links,subtext):
	hn = []
	for i,item in enumerate(links):
		title = item.getText()
		href = item.get("href",None)
		vote = subtext[i].select('.score')
		
		if len(vote):

			points = int(vote[0].getText().replace(' points',''))
			if points>99:
				hn.append({'title' : title,'link' : href, 'votes' : points})


	return sort_byvotes(hn)

pprint.pprint(custom_hn(mega_links,mega_subtext))