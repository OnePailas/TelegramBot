# Если будут планы работы с инлайн-кнопками, то писать блок кода для него надо до команды "/howay", в ином случае кнопки не будут работать

import telebot
from telebot import types
import time 

bot = telebot.TeleBot('6832812648:AAEiamzH7uhQTOLO1kuGHipb6AqX6oT6fVA')

@bot.message_handler(commands= ['start'])
def msgStart(message):
    bot.reply_to(message, 'Привет, этот бот создан начинающим программистом OnePailas для проверки своих спобностей. \
Ознакомиться со списком команд можно с помощью /help')

@bot.message_handler(commands= ['help'])
def msgHelp(message):
    bot.reply_to(message, 'А вот и список доступных команд: \n► /howay - данная команда спрашивает "Как Ваш дела". \n⫷⫷ПРИМЕЧАНИЕ⫸⫸ \n\
Если Вы хотите ответить положительным ответом, то используйте команду "/result" и ответы: хорошо, отлично. \nВ иных случаях: плохо, не очень \n\
► /umnichka - исследуй эту команду самостоятельно, уверяю, ты не пожалеешь\n\
► /time - данная команда указывает врем на данный момент')

#команда "Umnicka" нужна, чтобы просто поднять настроение, была создана новая команда, по функ мы ответили на команду таким сообщенем

@bot.message_handler(commands= ['umnichka'])
def msgUmnichka(message):
    bot.reply_to(message, 'Стой! Ты не знаешь кто умничка? Так это же ты, и даже не пытайся спорить со мной, я лучше знаю)')

# команда для вывода местного времени, позже надо будет доработать 

@bot.message_handler(commands= ['time'])
def msgTime(message):

    realTime = time.strftime('%m/%d/%Y %X', time.localtime())
    bot.reply_to(message, f'Время на данный момент: ' + realTime) 

#создается команда "HowAY, чтобы спросить как дела у пользователя и заранее даются ответы для развития общения с ботом, делается благодаря функции "func = lambda message: True"
#которая принимает сообщение пользователя, а уже с фунц "message.text" мы можем делать все, что угодно

@bot.message_handler(commands= ['howay'])
def howay(message):
    bot.send_message(message.chat.id, 'Кстати, а как твои дела?')

@bot.message_handler(func = lambda message: True)
def OtvHoway(message):

    pOtv = ['/result хорошо', '/result отлично']
    oOtv = ['/result плохо', '/result не очень']

    if message.text.lower() in pOtv:
        bot.reply_to(message, 'Супер, я рад за тебя')
    elif message.text.lower() in oOtv:
        bot.reply_to(message, 'Грустно, надеюсь в будущем у тебя станет все хорошо')
    else:
        bot.reply_to(message, 'Бот обрабатывает только команды и ответы на них. \
Используйте команды из списка, для их использования также обязательно писать "/"')

#был написан новый блок кода для распознавания фотографий. Тк целей нет для работы с изображениями, было добавлено уведомление, которое приходит, когда пользователь отправляет ресурс "фото"
#формат сообещния(фото, видео, гс, стик, сообщение) определяется с помощью модуля "content_types"

@bot.message_handler(content_types= ['photo'])
def msgPhoto(message):
    if message.photo:
        bot.send_message(message.chat.id, 'Бот не работает и не распознает изображения')

bot.polling()
