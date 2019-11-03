# price_bot

#### **Бот для телеграмма, показывает цену конкретного товара (по списку товаров).**

###### Bot for STRBT, checking adversarys price, and send current price to user

#### Блоки:
    
    
**- Парсер для сайта иструмента.**
    
Получает на вход экселевский файл с урлками тех товаров, по которым будет работать бот.
Экселевский файл может пополнятся пользователями, желающими добавить для сравнения новые позиции.
Урлы должны быть с двух сайтов (стройбат, инструмент)
Проходит по указанным урлкам, собирая цену товаров.
Пушит информцию в JSON-файл (поля: код Стройбата, название Стройбата, цена Стройбата, цена Инструмента)
    
    
**- Бот для работы с пользователем.**

Слушает чат телеграмма, к которому могут подключаться пользователи.
По цифровому запросу ползет в JSON-файл, смотрит наличие там товара, указанного пользователем.
Возвращает в ответе всю найденную в файле строку (название, цену Стройбата, цену инструмента).
В случае отсутствия кода в файле предлагает создать запрос на его добавление и дальнейшее отслеживание.


