# import telebot
# from telebot import types
# import random

# token = '6174814035:AAGniYRQkICFnY_zR6iIKj5oKY4S5enNrc4'

# bot = telebot.TeleBot(token)

# @bot.message_handler(commands=['start'])
# def start_message(message):
#     print('!!!!!!')
#     bot.send_message(message.chat.id, 'Bot started')
#     bot.register_next_step_handler(message, answer_text)

# def answer_text(message):
#     print(message.text, '!!!!!!')
#     if message.text.lower() == 'hi!':
#         bot.send_message(message.chat.id, 'Привет!')
#     elif message.text.lower()=='bye!':
#         bot.send_message(message.chat.id, 'Пока!')
#     bot.register_next_step_handler(message, answer_text)
  

    
    

# bot.polling()





# import telebot
# from telebot import types
# import random

# token = '6174814035:AAGniYRQkICFnY_zR6iIKj5oKY4S5enNrc4'

# bot = telebot.TeleBot(token)


# @bot.message_handler(commands=['start'])
# def start_message(message):
#     bot.send_message(message.chat.id, 'Bot started')
#     bot.send_message(message.chat.id, 'Введите своё ФИО:')
#     bot.register_next_step_handler(message, answer_user)

# def answer_user(message): #message.text == 'hi!'
#     bot.send_message(message.chat.id, f'Здравствуйте, {message.text}')
#     bot.send_message(message.chat.id, 'Test bot!')

# bot.polling()



import telebot
from telebot import types 
import random

token = '6174814035:AAGniYRQkICFnY_zR6iIKj5oKY4S5enNrc4'

bot = telebot.TeleBot(token)

Keyboard = types.ReplyKeyboardMarkup()
button1 = types.KeyboardButton('ИГРАТЬ')
button2 = types.KeyboardButton('НЕТ')
Keyboard.add(button1, button2)

@bot.message_handler(commands=['start', 'game'])
def start_message(message):
    message2 = bot.send_message(message.chat.id, 'привет, начнем игру?', reply_markup=Keyboard)
    bot.register_next_step_handler(message2, check_answer)


def check_answer(message):
    if message.text == 'ИГРАТЬ':
        bot.send_message(message.chat.id, 'Ок тогда вот правила: нужно угадать число от 1 до 10 за 3 попытки')
        number = random.choice(range(1, 11))
        game(message, 3, number)
    else:
        bot.send_message(message.chat.id, 'Хорошо, пока!')



def game(message, attempts, number):
    message2 = bot.send_message(message.chat.id, 'Введи число')
    bot.register_next_step_handler(message2, check_number, attempts-1, number)




def check_number(message, attempts, number):
    if message.text == str(number):
        bot.send_message(message.chat.id, 'Поздравляю, ты выиграл!!!')
        start_message(message)
    elif attempts == 0:
        bot.send_message(message.chat.id, 'Sorry Bro  у тя закончилсиь попытки')
        start_message(message)
    else:
        bot.send_message(message.chat.id, f'Не верно Bro, у тя осталось {attempts} попыток, попробуй еще раз ')
        game(message, attempts, number)



bot.polling()
