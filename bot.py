import json
import telebot
from telebot import types
import requests
import time
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot_token = "6261425349:AAHDit0-4gIUSHOBabfkARIuVWtjIIkXV_8"


bot = telebot.TeleBot(bot_token)
users = set()
users = {}


@bot.message_handler(commands=['start'])
def start_command(message):
    chat_id = message.chat.id
    bot.send_chat_action(chat_id, 'typing')
    bot.send_message(message.chat.id, "If you need further assistance, contact us through the support links provided in the start message. \n\n ተጨማሪ እርዳታ ከፈለጉ በመነሻ መልእክት ውስጥ በተሰጡት የድጋፍ ማገናኛዎች በኩል ያግኙን.",)


# Start the bot
bot.polling()
