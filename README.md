# price_bot
Bot for STRBT, checking adversary price, and send current price to user

Бот для телеграмма, анализирующий экселевскую таблицу и по запросу пользователя, показывает данные конкретного товара.

Блоки:
- Парсилка для сайта с адресами прокси.
Раз в час через crontab залезает на сайт с прокси адресами, находит нужные и пушит их в дата-файл в виде списка, отсортированного по пингу, начиная с наименьшего. 
Запихивает только те айпишники, к которым удается приконнектиться.
- Парсилка для сайта иструмента. 
Получает на вход экселевский файл с урлками тех товаров, по которым будет работать бот.
Экселевский файл может пополнятся пользователями, желающими добавить для сравнения новые позиции.
Урлы должны быть с двух сайтов (стройбат, инструмент)
Проходит по указанным урлкам, собирая цену товаров.
Пушит информцию в SQL-таблицу (поля: код Стройбата, название Стройбата, цена Стройбата, цена Инструмента)
- Бот для работы с пользователем.
Имеет доступ к дата-файлу, который содержит прокси-адреса, забирает отуда адреса для подключения к телеге.
Слушает чат телеграмма, к которому могут подключаться пользователи.
По цифровому запросу ползет в SQL-базу, смотрит наличие там товара, указанного пользователем.
Возвращает в ответе всю найденную в базе строку (название, цену Стройбата, цену инструмента).
