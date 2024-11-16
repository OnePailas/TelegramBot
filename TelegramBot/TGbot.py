import telebot

bot = telebot.TeleBot('6832812648:AAEiamzH7uhQTOLO1kuGHipb6AqX6oT6fVA')

@bot.message_handler(commands= ['start'])
def msgStart(message):
    bot.reply_to(message, 'Привет, этот бот создан начинающим программистом OnePaillas для проверки своих спобностей. Ознакомиться со списком команд можно с помощью "/help"')

@bot.message_handler(commands= ['help'])
def msgHelp(message):
    bot.reply_to(message, 'А вот и список доступных команд: \n► /HowAY - данная команда спрашивает "Как Ваш дела". \n⫷⫷ПРИМЕЧАНИЕ⫸⫸ \nЕсли Вы хотите ответить положительным ответом, то используйте слова: хорошо, прекрасно, нормально, чудесно, отлично. \nВ иных случаях: плохо, не очень, более-менее' \
        '\n► /Umnichka - исследуй эту команду самостоятельно, уверяю, ты не пожалеешь')

#команда "Umnicka" нужна, чтобы просто поднять настроение, была создана новая команда, по функ мы ответили на команду таким сообщенем

@bot.message_handler(commands= ['Umnichka'])
def msgUmnichka(message):
    bot.reply_to(message, 'Стой! Ты не знаешь кто умничка? Так это же ты, и даже не пытайся спорить со мной, я лучше знаю)')

#создается команда "HowAY, чтобы спросить как дела у пользователя и заранее даются ответы для развития общения с ботом, делается благодаря функции "func = lambda message: True"
#которая принимает сообщение пользователя, а уже с фунц "message.text" мы можем делать все, что угодно

@bot.message_handler(commands= ['HowAY'])
def msgHowAR(message):
    bot.reply_to(message, 'Кстати, а как твои дела?')
    
@bot.message_handler(func = lambda message: True)
def msgOtvetHowAY(message):

#здесь мы создаем списки с готовыми ответами, чтобы уменьшить код, но также учитывается ответ любого регистра, но определенного слова и кол-ва символов 

    otricOtvet = ['плохо', 'не очень', 'более-менее']
    polojitOtvet = ['хорошо', 'прекрасно', 'нормально', 'чудесно', 'отлично']
    otvetUser = message.text.lower()

    if otvetUser in polojitOtvet:
        bot.reply_to(message, 'Супер, я очень рад за тебя, надеюсь и в будущем у тебя будет все хорошо!')
        
    elif otvetUser in otricOtvet:
        bot.reply_to(message, 'Грустно, я очень надеюсь, что все придет к лучшему и ты будешь с улыбкой на лице. Знай, что  верю, ведь ты умничка, так ведь?')

bot.polling()