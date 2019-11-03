# ПАРСЕР ДЛЯ САЙТА СТРОЙБАТА
"""
Получает экселевский файл.
Первый столбик - id, второй - название, третий - урл стройбата, четверытй - урл инструмента
Считывает id-номер из первого столбика, название из второго и урлы из третьего и четвертого.
Последовательно (поэлементо) коннектиться к урлам, считывает информацию о цене для обоих сайтов.
Пушит их в 5 и 6 столбики соответственно)
Записывает в словарь данные, где ключ - id, значение - список со всей информацией.
"""

import pandas as pd
import requests
import json
from bs4 import BeautifulSoup as bs


def get_links_from_xlsx(price_dict):
    try:
        name = './../urls/urls.xlsx'
        # считываем из экселся, при этом обозначаем, что значение из столбца id строковое, чтобы не терять нули
        #  добавить в атрибуты pd.red   converters={'id': lambda x: str(x)}
        id_name_urls_dict = pd.read_excel(name, sheet_name='Sheet1')
        for i in range(len(id_name_urls_dict['id'])):
            id = str(id_name_urls_dict['id'][i])
            price_dict[id] = []
            price_dict[id].append(id_name_urls_dict['name'][i])
            price_dict[id].append(id_name_urls_dict['strbt_urls'][i])
            price_dict[id].append(id_name_urls_dict['instr_urls'][i])
            price_dict[id].append(0)
            price_dict[id].append(0)
    except FileNotFoundError:
        print('Error: no file fith urls in "./../urls/"')



def get_price_from_isntr_site(price_dict):
    headers = {
        'accpet': '*/*',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
    }
    for id, value in price_dict.items():
        clear_strbt_item_price = ''
        clear_instr_item_price = ''
        session = requests.Session()

        # блок парсинга стройбата
        try:
            request = session.get(price_dict[id][1], headers=headers)
            if request.status_code == 200:
                soup = bs(request.content, 'html.parser')
                strbt_element_name = soup.find('h1', itemprop='name').text
                price_dict[id][0] = strbt_element_name
                strbt_element_price = soup.find('span', class_='price').text
                for char in strbt_element_price:
                    if char.isdigit():
                        clear_strbt_item_price += char
                price_dict[id][3] = clear_strbt_item_price
            else:
                print('Connection error in strbt url')
        except:
            print('что-то пошло не так')
        # блок парсинга инструмента
        if 'http' not in str(price_dict[id][2]):
            price_dict[id][4] = 'У инструмента такой позиции на сайте нет'
            continue
        request = session.get(price_dict[id][2], headers=headers)
        if request.status_code == 200:
            soup = bs(request.content, 'html.parser')
            instr_element_price = soup.find('div', class_='product-view__price-value').text
            for char in instr_element_price:
                if char.isdigit():
                    clear_instr_item_price += char
            price_dict[id][4] = clear_instr_item_price
        else:
            print('Connection error ')#, in', price_dict[id][2], 'response =', request.status_code())





def push_price_dict_to_json(price_dict):
    with open("../dats/prices.json", "w", encoding='utf-8') as instr_price_json:
        json.dump(price_dict, instr_price_json, ensure_ascii=False, indent=4)



if __name__ == '__main__':
    price_dict = {}
    get_links_from_xlsx(price_dict)
    get_price_from_isntr_site(price_dict)

    for key, value in price_dict.items():
        print(key, value)

    push_price_dict_to_json(price_dict)
