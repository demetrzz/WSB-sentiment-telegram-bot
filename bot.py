import os
import telebot
from utils import get_data_from_api
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to WSB sentiment checker, pls type /sentiment to start")


@bot.message_handler(commands=['sentiment'])
def sign_handler(message):
    text = "Which ticker you wanna check? example: AMD, TSLA"
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, fetch_sentiment)


def fetch_sentiment(message):
    ticker = message.text.upper()
    horoscope = get_data_from_api()
    sentiment = [d["sentiment"] for d in horoscope if ticker == d["ticker"]]
    bot.send_message(message.chat.id, f'The sentiment is {sentiment}', parse_mode="Markdown")


@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, "Write /sentiment again if you want check another ticker")


bot.infinity_polling()
