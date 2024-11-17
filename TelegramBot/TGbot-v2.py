import telebot
from telebot import types

bot = telebot.TeleBot('6832812648:AAEiamzH7uhQTOLO1kuGHipb6AqX6oT6fVA')

@bot.message_handler(commands= ['start'])
def msgStart(message):
    otvetUser = message.text.lower()
    if otvetUser == '/start':
        bot.reply_to(message, 'Привет, этот бот создан начинающим программистом OnePailas для проверки своих спобностей. Ознакомиться со списком команд можно с помощью /help')
    else:
        bot.reply_to(message, 'Пожалуйста используйте команды из списка, для их использования также обязательно писать "/"')

@bot.message_handler(commands= ['help'])
def msgHelp(message):
    otvetUser = message.text.lower()
    if otvetUser == '/help':
        bot.reply_to(message, 'А вот и список доступных команд: \n► /howay - данная команда спрашивает "Как Ваш дела". \n⫷⫷ПРИМЕЧАНИЕ⫸⫸ \nЕсли Вы хотите ответить положительным ответом, то используйте слова: хорошо, прекрасно, нормально, чудесно, отлично. \nВ иных случаях: плохо, не очень, более-менее' \
        '\n► /umnichka - исследуй эту команду самостоятельно, уверяю, ты не пожалеешь')
    else:
        bot.reply_to(message, 'Пожалуйста используйте команды из списка, для их использования также обязательно писать "/"')

#команда "Umnicka" нужна, чтобы просто поднять настроение, была создана новая команда, по функ мы ответили на команду таким сообщенем

@bot.message_handler(commands= ['umnichka'])
def msgUmnichka(message):
    otvetUser = message.text.lower()
    if otvetUser == '/umnichka':
        bot.reply_to(message, 'Стой! Ты не знаешь кто умничка? Так это же ты, и даже не пытайся спорить со мной, я лучше знаю)')
    else:
        bot.reply_to(message, 'Пожалуйста используйте команды из списка, для их использования также обязательно писать "/"')

#создается команда "HowAY, чтобы спросить как дела у пользователя и заранее даются ответы для развития общения с ботом, делается благодаря функции "func = lambda message: True"
#которая принимает сообщение пользователя, а уже с фунц "message.text" мы можем делать все, что угодно

@bot.message_handler(commands= ['howay'])
def howay(message):
    bot.reply_to(message, 'кстати, а как твои дела?')

@bot.message_handler(func = lambda message: True)
def otvetHoway(message):

#здесь мы создаем списки с готовыми ответами, чтобы уменьшить код, но также учитывается ответ любого регистра, но определенного слова и кол-ва символов 

    polOtv = ['хорошо', 'отлично']
    otricOtv = ['плохо', 'не очень']
    msgUser = message.text.lower()

    if msgUser in polOtv:
        bot.reply_to(message, 'Супер, я рад за тебя')
    elif msgUser in otricOtv:
        bot.reply_to(message, 'Грустно, надеюсь в будущем у тебя станет все хорошо')
    else:
        bot.reply_to(message, 'Пожалуйста используйте команды из списка, для их использования также обязательно писать "/"')

#был написан новый блок кода для распознавания фотографий. Тк целей нет для работы с изображениями, было добавлено уведомление, которое приходит, когда пользователь отправляет ресурс "фото"
#формат сообещния(фото, видео, гс, стик, сообщение) определяется с помощью модуля "content_types"

@bot.message_handler(content_types= ['photo'])
def msgPhoto(message):
    if message.photo:
        bot.send_message(message.chat.id, 'Бот не работает и не распознает изображения')

bot.polling()
