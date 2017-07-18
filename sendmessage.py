import telebot
import settings
import work_db

bots = telebot.TeleBot(settings.TOKEN)
dic = work_db.Dictionary()
dic.send_mess(bots)
