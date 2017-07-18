# -*- coding: utf-8 -*-
import sqlite3
import sys
import time
from datetime import datetime



class DB():
    def __init__(self,name):
        self.name = name
        self.connect = sqlite3.connect(self.name)
        self.cursor = self.connect.cursor()

    def infoDB(self):
        sql = "SELECT name FROM sqlite_master WHERE type='table'"
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        print("Название базы данных: " + self.name)
        print("Таблицы: ")
        for self.row in rows:
            print(self.row[0])

    def infoUserDB(self):
        sql = "SELECT * FROM users"
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        print("Спискок пользователей: ")
        i = 0
        for self.row in rows:
            i += 1
            print(i,self.row[0], self.row[1])


    def delUserDB(self,user_name):
        sql = "DELETE FROM users WHERE name=?"
        self.cursor.execute(sql,[user_name])
        self.connect.commit()
        print("Пользователь удален")

    def add_dic(self, file):
        file_name = open(file, 'rb')
        line = file_name.readlines()
        k = 0
        for i in line:
            k += 1
            lines = i.decode('utf8')
            self.cursor.execute("""INSERT INTO dictionary VALUES ('%s','%s')"""%(k,i.decode('utf8')))
            self.connect.commit()
        print("Изменения в базу данных внесенно")







nameDB = "MyFunnyEnglish.db"
db = DB(nameDB)
# db.count()
print(datetime.now())
print('|===========================|')
print('|  Управление базой данных  |')
print('|===========================|')
print('| 1.Информация по базе      |')
print('| 2.Информация о users      |')
print('| 3.Удаление user-a         |')
print('| 4.Добавление слов         |')
print('| 0.Выход                   |')
print('|===========================|')
num = input("Ввидите цифру: ")
num = int(num)
if num == 1:
    db.infoDB()
elif num == 2:
    db.infoUserDB()
elif num == 3:
    user_name = input("Ввидите user-name: ")
    db.delUserDB(user_name)
elif num == 4:
    file_name = input("Ввидите имя файла: ")
    db.add_dic("1.txt")
elif num == 0:
    sys.exit()


