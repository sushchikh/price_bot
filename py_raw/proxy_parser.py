# Парсер для прокси адресов

"""
Чекает сайт с проксями. С предустановленными характеристиками (протокол HTTPS, пинг не больше 500 мс)
https://hidemy.name/ru/proxy-list/?maxtime=500&type=s&anon=4#list
Парсит сайт бютифулсупом, собиарет пары: айпишник и порт, соединяет это в один элемент.
Пушит элемет в список, если получает от него ответ 200.
Весь список пушит в датник.
"""


import requests
from bs4 import BeautifulSoup as bs
import datetime as dt


proxy_list_url = 'https://hidemy.name/ru/proxy-list/?maxtime=500&type=s&anon=4#list'
proxy_list_url = 'https://spys.one/sslproxy/'
proxy_list_url = 'https://198.211.96.170:3128'
# proxy_list_url = 'http://foxtools.ru/Proxy?al=True&am=True&ah=True&ahs=True&http=False&https=True'

# proxy_list_url = 'https://habr.com/ru/flows/geektimes/'
headers = {
    'accpet': '*/*',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}


def get_list_of_proxys(proxy_list_url, headers):
    session = requests.Session()
    request = session.get(proxy_list_url, headers=headers)
    print(request.status_code)
    if request.status_code == 200:
        # soup = bs(request.content, 'html.parser')
        print('Welldone')
    else:
        print('Connection error, cant reach proxy list site')


if __name__ == "__main__":
    get_list_of_proxys(proxy_list_url, headers)





