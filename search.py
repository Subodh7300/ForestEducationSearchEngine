from googleapiclient.discovery import build

FILTERS = {
    "default": "714ab3c8f48c042ce",
    "math": "c1e9fe4f1c4544778",
    "medicine": "226f18192d2054fd9",
    "personal-development": "15f7c414d15bb478f",
    "business": "27d24ed7b517e41b8",
    "sports": "55dc132a0dd4348cf",
    "programming-language": "5304bf24f663e4979",
    "computer": "9653c7ecd64dc4221",
    "engineer": "a4a4701ad06da48cb",
    "science": "c156bc9b20d344776",
    "health": "50877b7f8371c4d5c",
    "technology": "9315ded093b3e4ed6",
    "programming": "e6911b75693ea4ab0",
    "law": "1323d3b1e98eb4918",
    "courses": "b7e3e5eb2c01a4a5f",
    "books": "03fe812577a144246",
    "language": "074e7cfef2d4b4945"
}


class Search:
    def __init__(self, query: str, filter_str: str = "default"):
        self.API = 'AIzaSyAICgX5OJ09gd60JEKba6pPpFzs_ayULBw'
        # self.CX = FILTERS[filter_str]
        self.CX = "714ab3c8f48c042ce"
        self.query = query
        self.resource = build('customsearch', 'v1', developerKey=self.API).cse()
        self.startIndex = 1

    def show_page(self, page_count: int):
        self.startIndex = page_count*10 + 1
        ls = self.resource.list(q=self.query, cx=self.CX, start=self.startIndex).execute()
        print(ls['items'])
        return ls['items']

    def img_page(self, page_count: int):
        self.startIndex = page_count*10 + 1
        ls = self.resource.list(q=self.query, cx=self.CX, start=self.startIndex, searchType='image').execute()
        return ls['items']
