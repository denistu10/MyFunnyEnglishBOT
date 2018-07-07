import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

TOKEN = "" #Токен для Telegram-бота

DB_HOST = 'localhost'
DB_NAME = os.path.join(BASE_DIR, 'MyFunnyEnglish.db')


TMP_FILE = '/tmp/bot.txt'
LOG_FILE = '/tmp/bot.log'