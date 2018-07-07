#!/usr/bin/env python3.6

import telebot
import settings
import db


bots = telebot.TeleBot(settings.TOKEN)
dic = db.Dictionary(settings.DB_NAME)
dic.send_mess(bots)
