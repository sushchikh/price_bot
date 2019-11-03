"""
Жует жсон с ценами (в режиме чтения)
Слушает канал телеграмма на предмет появления новых сообщений
Если не цифрововй код - отвечает ошибкой о том, что нужно ввести цифровой айди товара
Если код цифровой, пытается найти его в словаре, полученном из жсона с ценами.
Если находит - выдает цены, если не находит выдает сообщение об отсутствии информции по этому товару и
и предлагает добавить этот товар в список отслеживаемых

"""
import telebot
import json
import datetime
import random
########     ###    ########    ###
##     ##   ## ##      ##      ## ##
##     ##  ##   ##     ##     ##   ##
##     ## ##     ##    ##    ##     ##
##     ## #########    ##    #########
##     ## ##     ##    ##    ##     ##
########  ##     ##    ##    ##     ##


with open('../dats/prices.json', 'r') as f:
    prices_dict = json.load(f)


########   #######  ########
##     ## ##     ##    ##
##     ## ##     ##    ##
########  ##     ##    ##
##     ## ##     ##    ##
##     ## ##     ##    ##
########   #######     ##

token = '1017086391:AAHva9tCXNysdsvnVVxtscrgTAN7bdPSWA4'


bot = telebot.TeleBot('1017086391:AAHva9tCXNysdsvnVVxtscrgTAN7bdPSWA4')
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('доступные команды', 'some')
today = datetime.datetime.now().strftime('%d.%m.%y')
list_of_request_id = {str(today): []}
logs_dict = {str(today): []}

stickers = {
    'utka': [
        'CAADAgADBAEAAladvQreBNF6Zmb3bBYE',
        'CAADAgAD_gADVp29CtoEYTAu-df_FgQ',
        'CAADAgAD9gADVp29CvfbTiFAPqWKFgQ',
        'CAADAgAD9wADVp29CgtyJB1I9A0wFgQ',
        'CAADAgAD-QADVp29CpVlbqsqKxs2FgQ',
        'CAADAgAD-wADVp29ClYO2zPbysnmFgQ',
        'CAADAgADDQEAAladvQpG_UMdBUTXlxYE',
        'CAADAgADDgEAAladvQoRqS1ownHgaBYE']
}



@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

@bot.message_handler(content_types=['sticker'])
def sticker_id(message):

    print(message)

@bot.message_handler(content_types=['text'])
def send_text(message):
    logs_dict[today] = message.text
    with open('../dats/logs.json', 'a') as logs:
        json.dump(logs_dict, logs, ensure_ascii=False, indent=4)
    try:
        request_id = int(message.text)
        print(message.text)
        id = str(int(message.text))  # убираем первые ноли, если пользователь ввел код в формте 00001234*
        # print(prices_dict.get(id))
        if str(prices_dict[id][4]) == 'У инструмента такой позиции на сайте нет':
            output_message = str(str(request_id)+ "\n" + prices_dict[id][0]) + '\n' + 'Cтройбат: ' + str(prices_dict[id][3]) + ' .р' + '\n' + 'У инструмента такой позиции на сайте нет'
        else:
            output_message = str(str(request_id)+ "\n" + prices_dict[id][0]) + '\n' + 'Cтройбат: ' + str(prices_dict[id][3]) + ' .р' + '\n' + 'Инструмент: ' + str(prices_dict[id][4] + ' .p')
        bot.send_message(message.chat.id, output_message)
    except ValueError:
        bot.send_message(message.chat.id, 'Вы ввели не код товара')
    except KeyError:
        bot.send_message(message.chat.id, 'Такого товара нет в отслеживаемом списке,\nесли хотите, чтобы я следил и за его ценой - введите "да"')
        list_of_request_id[today].append(message.text)
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, сотрудник стройбата!')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, сотрудник стройбата!')
    elif message.text.lower() == 'да':
        output_message = 'Я передам своему создателю, что вы хотите контролировать цену товара с кодом\n' + str(list_of_request_id[today][-1])
        bot.send_message(message.chat.id, output_message)
        with open('../dats/id_for_tracking.json', 'a') as id_for_tracking:
            json.dump(list_of_request_id, id_for_tracking, ensure_ascii=False, indent=4)
    elif message.text.lower() == 'утя' or message.text.lower() == 'уточка' or message.text.lower() == 'уточку' or message.text.lower() == 'утку' or message.text.lower() == 'утка':
        bot.send_sticker(message.chat.id, str(stickers['utka'][random.randint(0, 7)]))

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)

bot.polling()