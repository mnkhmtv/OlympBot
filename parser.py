import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


URL_TEMPLATE = "https://olimpiada.ru/article/992#iikt"
r = requests.get(URL_TEMPLATE)
# print(r.status_code)


soup = bs(r.text, "html.parser")
olympiads_names_all = soup.find_all('div', class_='standart_text_block')


for name in olympiads_names_all:
    olympiad_names = soup.find_all('table', class_='slim_dec')
    print(olympiad_names)
