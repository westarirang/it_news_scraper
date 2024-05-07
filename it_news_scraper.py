import requests
from bs4 import BeautifulSoup
import json
import os
import sys
import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
current_date = datetime.datetime.now().strftime("%Y%m%d")
file_name = f'it_news_{current_date}.json'

print('스크래핑 시작')

req = requests.get('https://www.itworld.co.kr/news')
req.encoding= None
html = req.content
soup = BeautifulSoup(html, 'html.parser')
datas = soup.select(
    '.section-content .node-list h5'    
)

data = {}

for title in datas:   
    name = title.find_all('a')[0].text
    url = 'https://www.itworld.co.kr'+title.find('a')['href']
    data[name] = url

with open(os.path.join(BASE_DIR, file_name), 'w+',encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii = False, indent='\t')

print('스크래핑 끝')