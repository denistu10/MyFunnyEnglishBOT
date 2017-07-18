import telebot
from settings import *
from datetime import datetime
import work_db


bot = telebot.TeleBot(TOKEN)

START = "Добро пожаловать, здесь ты можешь изучить более 1000 английских слов\n" \
        "Welcome, here you can learn more than 1000 English words"
HELP = "Для того чтобы начать пользовать ботом, вам нужно добавить себя в рассылку.\n" \
       "Делается это командой /add . После чего вам каждый день в определенное время будет приходить 5 различных слов\n" \
       "Если вы по каким то причинам хотите удалить себя из рассылки бота, используйте команду /remove ."



def log(message, answer):
    file_log = open("bot.log", 'a')
    file_log.writelines(str(datetime.now()) + " " + "Сообщение от: {0} {1}. (id = {2}) Текст:{3} \n".format(message.from_user.first_name,
                                                                   message.from_user.last_name,
                                                                   str(message.from_user.id),
                                                                   message.text))
    print((str(datetime.now()) + " " + "Сообщение от: {0} {1}. (id = {2}) Текст: {3} \n".format(message.from_user.first_name,
                                                                   message.from_user.last_name,
                                                                   str(message.from_user.id),
                                                                   message.text)))

@bot.message_handler(commands=["start"])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    user_markup.row("/add", "/remove", "/help")
    bot.send_message(message.from_user.id, START, reply_markup=user_markup)
    answer = START
    log(message, answer)


@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.send_message(message.chat.id, HELP)
    answer = HELP
    log(message, answer)



@bot.message_handler(commands=['add'])
def handle_add(message):
    users = message.from_user.first_name + " " + message.from_user.last_name
    chatID = message.from_user.id
    # users.addDB(users, chatID)
    sucs = "Вы добавлены в базу рассылки бота\n" \
           "You are added to the bot mailing list"
    bot.send_message(message.chat.id, sucs)
    log(message, sucs)



@bot.message_handler(commands=['remove'])
def handle_remove(message):
    chatID = message.from_user.id
    # users.delete_userdb(chatID)
    sucs = "Вы удалены из базы рассылки бота\n" \
           "You are removed from the bot mailing list"
    bot.send_message(message.chat.id, sucs)
    log(message, sucs)


users = work_db.User()
bot.polling(none_stop=True, interval=0)


# input()

def main():
    pass


if __name__ == '__main__':
    main()