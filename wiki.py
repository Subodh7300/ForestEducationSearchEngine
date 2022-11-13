import requests
from bs4 import BeautifulSoup


class Wiki:
    def __init__(self, query):
        query = query
        api = 'AIzaSyAICgX5OJ09gd60JEKba6pPpFzs_ayULBw'
        self.url = f'https://customsearch.googleapis.com/customsearch/v1?cx=714ab3c8f48c042ce&num=1&q=' \
                   f'{query}&siteSearch=wikipedia.org&siteSearchFilter=i&key={api}'

    def data(self):
        response = requests.get(url=self.url)
        if response.status_code == 200:
            try:
                soup = BeautifulSoup(response.content, 'html.parser')
                para = soup.find(id='bodyContent').find_all('p')[1]
                img = soup.find(class_='infobox-image').find_all('img')[0]['src']

                return para, img
            except:
                return "", ""
        else:
            return "", ""
