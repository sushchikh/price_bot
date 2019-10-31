# ПАРСЕР ДЛЯ САЙТА ИНСТРУМЕНТА
"""
Получает экселевский файл. В числе прочих 3 столбик содержит перечень ссылок, которые должны быть запарсены.
Считывает id-номер из первого столбика и урлы из третьего.
Последовательно (поэлементо) коннектиться к урлам, считывает информацию о цене.
Записывает в словарь данные, где ключ - id, значение - цена.
"""

import pandas as pd
import requests
from bs4 import BeautifulSoup as bs


def get_links_from_xlsx():
    urls_dict = {}
    try:
        name = './../urls/urls.xlsx'
        instr_urls_df = pd.read_excel(name, sheet_name='Sheet1')
        for i in range(len(instr_urls_df['id'])):
            urls_dict[instr_urls_df['id'][i]] = instr_urls_df['instr_urls'][i]
        for key, value in urls_dict.items():
            print(key, value)
    except FileNotFoundError:
        print('Error: no file fith urls in "./../urls/"')

def get_price_from_isntr_site(urls_list):
    headers = {
        'accpet': '*/*',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
    }
    for url_adress in urls_list:
        clear_item_price = ''

        session = requests.Session()
        request = session.get(url_adress, headers=headers)
        if request.status_code == 200:
            soup = bs(request.content, 'html.parser')
            element_price = soup.find('div', class_='product-view__price-value').text
            for char in element_price:
                if char.isdigit():
                    clear_item_price += char
            print(clear_item_price)

        else:
            print('Connection error, in', url_adress, 'response =', request.status_codes())



if __name__ == '__main__':
    instr_urls_list = []
    get_links_from_xlsx()
    get_price_from_isntr_site(instr_urls_list)
    # фукция считывания экселевского файла в датафрейм.
    # функция парсинга сайта и создание словаря, пуш словаря в датник
