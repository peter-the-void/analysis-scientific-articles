import urllib.request
import urllib.error
from bs4 import BeautifulSoup
import threading
_url = 'http://cyberleninka.ru/article'

def get_html(url):
	response = urllib.request.urlopen(url)
	return response.read()


def get_number_of_last_page(url):
	soup = BeautifulSoup(get_html(url))
	for link in soup.find_all('a',class_='last link-page'):
		return int(link.get('page'))


def parse_category(url):
	category_list = list()
	soup = BeautifulSoup(get_html(url))
	catalog = soup.find('div', class_='catalog-article')
	for group in catalog.find_all('li')[2:]:
		if group.a is not None:
			category_list.append((group.a.get_text(),'http://cyberleninka.ru' + group.a.get('href')))	
	return category_list


def get_articles_urls(url):
	articles_urls = list()
	for i in range(1,get_number_of_last_page(url)+1):
		soup = BeautifulSoup(get_html(url+'/'+str(i)))
		for article in soup.find_all('span', class_='heading-text'):
			if article.a is not None:
				art_links = 'http://cyberleninka.ru' + article.a.get('href')
			articles_urls.append(art_links)
		print(url+'/'+str(i))
	return articles_urls


def parse_articles(urls_list):
	pass


def main():
	q = parse_category(_url)
	print(get_articles_urls(q[0][1]))


if __name__ == '__main__':
	main()

