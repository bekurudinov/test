from parse import parse_news
import telebot
from telebot import types
import  json


token = '6174814035:AAGniYRQkICFnY_zR6iIKj5oKY4S5enNrc4'

bot = telebot.TeleBot(token)

keyboard = types.ReplyKeyboardMarkup()
button1 = types.KeyboardButton('Фото')
button2 = types.KeyboardButton('описание')
keyboard.add(button1, button2)
def read_news():
    with open('data.json')as file:
        data = json.load(file)
    return data



read_news()

@bot.message_handler(commands=['start'])
def start_parse(message):
    print('!!!!!!!!!!!!!!!!')
    bot.send_message(message.chat.id, 'Бот приветсвует вас , мы начали парсинг!\nПодождите пару секунд...')
    print('started')
    parse_news()
    print('parsed')
    data = read_news()
    print(data)
    for x in data:
        print(x)
        bot.send_message(message.chat.id, f'{x}--> {data [x]["title"]}')


    message_from_bot = bot.send_message(message.chat.id,'Нужно  число выбрать новости для для подробной тнформации(1-20): ')
    bot.register_next_step_handler(message_from_bot,check_number)

def check_number(message):
    keys = [str(x) for x in range(1, 21)]
    if message.text not in keys:
        print(message.text)
        message_from_bot = bot.send_message(message.chat.id,'Неверное число, Нужно выбрать число от(1-20): ')
        bot.register_next_step_handler(message_from_bot,check_number)
    else:
        data = read_news()
        message_from_bot=bot.send_message(message.chat.id, f'{data[message.text] ["title"]}\n Выберите фото или описание этой новости!', reply_markup=keyboard)
        bot.register_next_step_handler(message_from_bot, show_info, message.text,data)


def show_info(message, number,data):
    if  message.text == 'Фото':
        bot.send_message(message.chat.id, data[number]['img'])
        message_from_bot = bot.send_message(message.chat.id,'Нужно  число выбрать новости для для подробной тнформации(1-20): ')
        bot.register_next_step_handler(message_from_bot,check_number)
        

    else:
        bot.send_message(message.chat.id, data[number]['desc'])
        message_from_bot = bot.send_message(message.chat.id,'Нужно  число выбрать новости для для подробной тнформации(1-20): ')
        bot.register_next_step_handler(message_from_bot,check_number)
       

        



bot.polling()
