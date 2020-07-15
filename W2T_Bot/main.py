import telebot
from datetime import datetime
from config import TG_TOKEN
from config import datatable
from config import deltable

bot = telebot.TeleBot(TG_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    send_mess = f"<b>{message.from_user.first_name} , Добрый день</b>.\n" \
                f"Я - бот принимающий заявки. Я предназначен для помощи людям у которых есть поток клиентов," \
                f" которых они не успевают записать на приём/сеанс/консульрацию и т.п.\n" \
                f"Чтобы начать работу, напишите команду /help"
    bot.send_message(message.chat.id, send_mess, parse_mode='html')

@bot.message_handler(commands=['help'])
def help(message):
    send_mess = f"Добро пожаловать\nСписок доступных команд:\n/start - начало работы бота\n " \
                f"/add - записаться на консультацию\n/del - отмена записи\n "
    bot.send_message(message.chat.id, send_mess, parse_mode='html')
@bot.message_handler(commands=['add'])
def add(message):
    send_mess = f"Вы решили записаться на консультацию. Для этого потребуются ваше ФИО и номер телефона\nВведите " \
                f"команду /addme и ваше ФИО и телефон\n<b>Пример: </b> /addme Иванов Иван Иванович 8 777 666 55 44"
    bot.send_message(message.chat.id, send_mess, parse_mode='html')

@bot.message_handler(commands=['addme'])
def addme(message):
    pos = message.text.find("addme") + 6
    txt = message.text[pos:]
    today = datetime.today().strftime("%d-%m-%Y\n")
    patch = 'datatable'
    file = open(patch, 'a')
    file.write(today)
    file.write("%s\n-------------------------------------\n" % txt)
    file.close()
    send_mess = f"Вы успешно записались\nОжидайте звонка нашего сотрудника\nЕсли вы по каким-либо причинам захотите " \
                "отменить запись, наберите команду /del"
    bot.send_message(message.chat.id, send_mess, parse_mode='html')

@bot.message_handler(commands=['del'])
def dell(message):
    send_mess = f"Вы решили отменить свою запись. Для этого нужно ввести ваше ФИО и номер телефона\nВведите " \
                f"команду /delme и ваше ФИО и телефон, после чего ваша запись анулируется\n" \
                f"<b>Пример: </b> /delme Иванов Иван Иванович 8 777 666 55 44"
    bot.send_message(message.chat.id, send_mess, parse_mode='html')

@bot.message_handler(commands=['delme'])
def dellme(message):
    pos = message.text.find("delme") + 6
    txt = message.text[pos:]
    today = datetime.today().strftime("%d-%m-%Y\n")
    patch = 'deltable'
    delfile = open(patch, 'a')
    delfile.write(today)
    delfile.write("Данный пользователь отменил запись!\n")
    delfile.write("%s\n-------------------------------------\n" % txt)
    delfile.close()
    send_mess = f"Ваша запись отменена\nЕсли передумаете, повторите запрос при помощи команды /addme"
    bot.send_message(message.chat.id, send_mess, parse_mode='html')

@bot.message_handler(content_types=['text'])
def unknown_command(message):
    if "/" in message.text:
        send_mess = f"Это неизвестная для меня команда\nЧтобы получить список доступных команд напишите /help"
    else:
        send_mess = f"Добрый день. Для начала работы напишите команду /start"
    bot.send_message(message.chat.id, send_mess, parse_mode='html')

bot.polling(none_stop=True, interval=0)