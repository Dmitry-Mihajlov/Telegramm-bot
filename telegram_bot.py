import telebot
from telebot import types
from telegram_bot_open import OPEN_NAMES_TASKS, OPEN_CATALOG
from telegram_bot_text import TEXT_START, TEXT_HELP, TEXT_INFO
from telegram_bot_names_tasks import KEYBOARD
bot = telebot.TeleBot('token')



@bot.message_handler(commands=['start'])
def start(message):
    """Выводит начальное приветствие и дает команды которые можно использовать"""
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_1 = types.KeyboardButton(text='/catalog')
    btn_2 = types.KeyboardButton(text='/help')
    kb.add(btn_1, btn_2)

    bot.send_message(message.chat.id, TEXT_START(message), reply_markup=kb)



@bot.message_handler(commands=['help'])
def help(message):
    """Выводит просто текст"""
    bot.send_message(message.chat.id, TEXT_HELP(message))


@bot.message_handler(commands=['info'])
def info(message):
    """Выводит просто текст"""
    bot.send_message(message.chat.id, TEXT_INFO(message))



@bot.message_handler(commands=['catalog'])
def names_tasks(message):
    """Выводим названия задач"""
    names_tasks_list = OPEN_NAMES_TASKS()
    bot.send_message(message.chat.id, 'Доступные задания:')
    bot.send_message(message.chat.id, ''.join(names_tasks_list), reply_markup=KEYBOARD(message))

@bot.callback_query_handler(func=lambda callback: callback.data)
def task(callback):
    """Выводим задание"""

    if callback.data == '0': user_response = 0
    elif callback.data == '1': user_response = 1
    elif callback.data == '2': user_response = 2
    elif callback.data == '3': user_response = 3
    elif callback.data == '4': user_response = 4
    elif callback.data == '5': user_response = 5
    elif callback.data == '6': user_response = 6
    elif callback.data == '7': user_response = 7
    elif callback.data == '8': user_response = 8
    elif callback.data == '9': user_response = 9

    catalog_zd_list = OPEN_CATALOG()
    bot.send_message(callback.message.chat.id, f'{catalog_zd_list[user_response]}\nОтветом является число.')




@bot.message_handler(content_types=['text'])
def Except(message):
    bot.send_message(message.chat.id, 
    'Упс, что-то не так.\n'
    'Используй интерактивную клавиатуру.\n'
    'Если возникли вопросы, то отправь команду /help')


@bot.message_handler(content_types=['sticker'])
def stiker(message):
    sticker = open(r'D:\Programming\function_per_hundred_bot\AnimatedSticker_sticker.tgs', "rb")
    bot.send_sticker(message.chat.id, sticker)

@bot.message_handler(content_types=['photo'])
def photo(message):
    photo = open(r'D:\Programming\function_per_hundred_bot\AnimatedSticker_foto.tgs', "rb")
    bot.send_sticker(message.chat.id, photo)

bot.polling(non_stop=True)
