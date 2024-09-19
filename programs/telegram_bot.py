# Пишем Простейший Телеграм Бот
# В телеграме есть официальной бот для управления своими ботами - https://t.me/BotFather
# Токен для моего бота KondrichBot - 7917452908:AAGTcX-y3QWliJM4hdszIlA8E2bqJxk3GXQ

# pip install ->
# pyTelegramBotAPI

from telebot import TeleBot

TOKEN = "7917452908:AAGTcX-y3QWliJM4hdszIlA8E2bqJxk3GXQ"

# создаем екзепляр класса TeleBot
bot = TeleBot(TOKEN)

# commands указывает какие команды в боте мы будем обрабатывать от пользователя
@bot.message_handler(commands=["start","help"])
