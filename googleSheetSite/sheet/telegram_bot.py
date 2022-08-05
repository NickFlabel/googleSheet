import telebot
from .models import Chat
from django.db.utils import IntegrityError

token = '5542517598:AAHgBzoLXBs51R3-gfEOba7VntsBZdEL1Aw'   #Telegram token

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    """Starts the chat and memorizes the chat id for further messaging
    """
    bot.send_message(message.chat.id, 'Здравствуйте! Вы подписались на рассылку по заказам. Если вы больше не хотите получать сообщения, введите /stop.')
    try:
        new_chat = Chat.objects.create(chat_id_tel=message.chat.id)
        new_chat.save()
    except IntegrityError:
        pass


@bot.message_handler(commands=['stop'])
def stop(message):
    """Stops the chat and deletes it from the db
    """
    bot.send_message(message.chat.id, 'Работа остановлена')
    chat = Chat.objects.get(chat_id_tel=message.chat.id)
    chat.delete()


