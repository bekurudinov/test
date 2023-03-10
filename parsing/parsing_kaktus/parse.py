from bs4 import BeautifulSoup as bs
import requests
import csv
import json


def get_html(url):
    response = requests.get(url)
    return response.text

def get_soup(html):
    return bs(html, 'lxml')

def get_catalog(html):
    soup = get_soup(html)
    catalog = soup.find('div', class_ ='Tag--articles')
    return catalog


def get_articles(catalog):
    articles = catalog.find_all('div', class_ ='Tag--article')
    while len(articles) > 20:
        articles.pop()
    return articles


def get_detail(link):
    from functools import reduce
    html = get_html(link)
    soup =get_soup(html)
    container = soup.find('div', class_='BbCode')
    text = container.find_all('p')
    res = reduce(lambda a, b: a + b, (x.text for x in text))
    return res

def get_data(articles):
    i = 1
    res ={}
    for item in articles:
        title = item.find('a', class_ ='ArticleItem--name').text.strip()
        image = item.find('img', class_='ArticleItem--image-img').get('src')
        image = image.replace('small', 'big')
        link = item.find('a', class_='ArticleItem--name').get('href')
        description = get_detail(link)
        data = {'title': title, 'img': image, 'desc': description}
        res[i] = data
        i += 1
    return res        


def write_to_json(data):
    with open ('data.json', 'w')as file:
        json.dump(data, file, ensure_ascii=False, indent=4)



def parse_news():
    base_url = 'https://kaktus.media/?lable=8&date=2023-02-01&order=time'
    html = get_html(base_url)
    articles = get_articles(get_catalog(html))
    data = get_data(articles)
    write_to_json(data)

if __name__ == '__main__':
    parse_news()
