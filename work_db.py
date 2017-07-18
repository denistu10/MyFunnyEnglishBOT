import sqlite3
import telebot
import settings

class User():
    #Фун-ция создания БД
    def createDb(self):
        connect = sqlite3.connect("MyFunnyEnglish.db")
        cursor = connect.cursor()
        cursor.execute("""CREATE TABLE users(name text, chatId integer)""")
        connect.commit()

    def addDB(self, user, chatid):
        #Добавление пользователя телеграм в базу, получаемые от обработчика команды "add'
        self.user = user
        self.chatID = chatid
        connect = sqlite3.connect("MyFunnyEnglish.db")
        cursor = connect.cursor()
        cursor.execute("""INSERT INTO users VALUES ('%s','%s')"""%(self.user,self.chatID))
        connect.commit()

    def delete_userdb(self,chatID):
        # Удаление пользователя телеграм в базе, получаемые от обработчика команды "remove'
        self.chatid = chatID
        connect = sqlite3.connect("MyFunnyEnglish.db")
        cursor = connect.cursor()
        sql = "DELETE FROM users WHERE chatId=?"
        cursor.execute(sql,[self.chatid])
        connect.commit()

    def infoUserDB(self):
        #Получаем все  из table user
        connect = sqlite3.connect("MyFunnyEnglish.db")
        cursor = connect.cursor()
        sql = "SELECT * FROM users"
        cursor.execute(sql)
        rows = cursor.fetchall()
        return rows

class Dictionary():
    file = open("temp.txt")
    txt = file.readlines()
    count = int(txt[0])
    def set_phr(self):
        connect = sqlite3.connect("MyFunnyEnglish.db")
        cursor = connect.cursor()
        sql = "SELECT * FROM dictionary WHERE id=?"
        row = []
        for i in range(self.count, self.count + 5):
            ids = i
            cursor.execute(sql, [ids])
            rows = cursor.fetchall()
            # self.count += 5
            wr = open("temp.txt", "w")
            new_num = str(i + 1)
            wr.write(new_num)
            wr.close()
            for k in rows:
                row.append(k)
        return row


    def send_mess(self,bot):
        users = user.infoUserDB()
        temp = self.set_phr()
        for chatid in users:
            for tem in temp:
                bot.send_message(chatid[1],tem[1])


user = User()