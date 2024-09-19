# Пишем Простейший Телеграм Бот
# В телеграме есть официальной бот для управления своими ботами - https://t.me/BotFather
# Токен для моего бота KondrichBot - 7917452908:AAGTcX-y3QWliJM4hdszIlA8E2bqJxk3GXQ

# -- pip install -->
# pyTelegramBotAPI
# requests

# pyTelegramBotAPI
from telebot import TeleBot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

# requests
import requests

TOKEN = "7917452908:AAGTcX-y3QWliJM4hdszIlA8E2bqJxk3GXQ"

# создаем екзепляр класса TeleBot, какбы создаем нашаего бота в пайтоне
# будем работать с нашим ботом через его название my_bot
my_bot = TeleBot(TOKEN)

# значения криптовалют для взаемодейтсвия с api binance
CRYPTO_NAME_TO_TICKER = {
    "Bitcoin": "BTCUSDT",
    "Ethereum": "ETHUSDT",
    "Doge": "DOGEUSDT",
}


# /start
@my_bot.message_handler(commands=["start"])
def send_welcome(message):
    # создание разметки для кнопок
    # row_width хранит количество места для кнопок, поместиться 3 кнопки
    markup = ReplyKeyboardMarkup(row_width=3)
    for crypto_name in CRYPTO_NAME_TO_TICKER.keys():
        # создание кнопок
        item_button = KeyboardButton(crypto_name)
        # добавление в разметку новосозданых кнопок
        markup.add(item_button)
    # message.chat.id хранит текущий номер чата
    # "Choose a crypto name" хранит текст, которым бот ответит в чате пользователю
    # reply_markup указывате будем ли использовать область с кнопками, елси да то указываем ету область
    my_bot.send_message(message.chat.id, "Choose a crypto name", reply_markup=markup)


# обабатывает нажатия пользователя на наши кнопки
@my_bot.message_handler(
    func=lambda message: message.text in CRYPTO_NAME_TO_TICKER.keys()
)
def send_price(message):
    crypto_name = message.text
    # ticker хранит значения  "BTCUSDT" , "ETHUSDT" , "DOGEUSDT"
    ticker = CRYPTO_NAME_TO_TICKER[crypto_name]
    price = get_price_by_ticker(ticker=ticker)
    my_bot.send_message(
        message.chat.id, f"Price of {crypto_name} to USDT is {price} right now"
    )


# функция берет значение крипты к долару из сайта biance по api
def get_price_by_ticker(*, ticker: str):
    endpoint = "https://api.binance.com/api/v3/ticker/price"
    params = {
        "symbol": ticker,
    }
    response = requests.get(url=endpoint, params=params)
    data = response.json()
    # 2 означает количество цифер после комы
    price = round(float(data["price"]), 2)

    return price


# commands указывает какие команды в боте мы будем обрабатывать от пользователя
# /start   /help
# @my_bot.message_handler(commands=["start", "help"])
# def send_welcome(message):
#     # message хранит всю информацию о пользователе, который написал что-то в чат бота
#     print(message)
#     # даем ответ пользователю в чате
#     my_bot.reply_to(message, "Hello, how are doing?")


# бот будет обрабатывать любые команды и текст, которые написал пользователь в чате
# @my_bot.message_handler(func=lambda message: True)
# def echo_all(message):
#     print(message)
#     # message.text хранит тотже текст, который написал пользователь в чате за один текущий раз
#     my_bot.reply_to(message, message.text)


# запуск бота на локальном сервера, когда запущен наш код только тогда работает бот
my_bot.infinity_polling()
