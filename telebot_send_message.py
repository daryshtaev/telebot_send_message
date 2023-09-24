# https://github.com/daryshtaev/telebot_send_message
# ver. 1.0.0

import telebot
def bot_send_message(bot_token, chat_id, msg='', parse_mode=None, msg_size_limit=4096):
    bot = telebot.TeleBot(bot_token);
    # import telebot (pyTelegramBotAPI)
    # Если длина текста сообщения превышает допустимый лимит (4096 символов), тогда разбиваем текст на несколько сообщений.
    if len(msg) > msg_size_limit:
        for x in range(0, len(msg), msg_size_limit):
            bot.send_message(chat_id, msg[x:x+msg_size_limit], parse_mode=parse_mode)
    else:
        bot.send_message(chat_id, msg, parse_mode=parse_mode)
