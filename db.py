import sqlite3

class User():
    def __init__(self, db):
        self.db = db

    def addDB(self, user, chat_id):
        self.user = user
        self.chat_id = chat_id
        connect = sqlite3.connect(self.db)
        cursor = connect.cursor()
        cursor.execute("""INSERT INTO users VALUES ('%s','%d')""" % (self.user,self.chat_id))
        connect.commit()

    def delete_userdb(self, chat_id):
        # Удаление пользователя телеграм в базе, получаемые от обработчика команды "remove'
        self.chatid = chat_id
        connect = sqlite3.connect(self.db)
        cursor = connect.cursor()
        sql = "DELETE FROM users WHERE chatId=?"
        cursor.execute(sql,[self.chatid])
        connect.commit()

    def infoUserDB(self):
        #Получаем все из table user
        connect = sqlite3.connect(self.db)
        cursor = connect.cursor()
        sql = "SELECT * FROM users"
        cursor.execute(sql)
        rows = cursor.fetchall()
        return rows


class Dictionary():
    file = open("temp.txt")
    txt = file.readlines()
    count = int(txt[0])

    def __init__(self, db):
        self.db = db


    def set_phr(self):
        connect = sqlite3.connect(self.db)
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
        user = User("MyFunnyEnglish.db")
        users = user.infoUserDB()
        temp = self.set_phr()
        for chatid in users:
            for tem in temp:
                bot.send_message(chatid[1],tem[1])
