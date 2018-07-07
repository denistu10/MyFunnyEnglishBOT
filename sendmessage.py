#!/usr/bin/env python3.6

import telebot
import settings
import db


bots = telebot.TeleBot(settings.TOKEN)
dic = db.Dictionary("MyFunnyEnglish.db")
dic.send_mess(bots)
