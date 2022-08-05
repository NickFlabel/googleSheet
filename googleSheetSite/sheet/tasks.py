from .utils import fetch_sheet, select_due_orders
from .models import Sheet, Chat
from celery import current_app
from .telegram_bot import bot
from celery.schedules import crontab

app = current_app._get_current_object()  # Gets current working celery app object


@app.task
def save_sheet_in_the_db():
    """This function fetches the data from google sheet and adds it into the database
    """
    Sheet.objects.all().delete()
    values = fetch_sheet()
    for value in values:
        order = Sheet.objects.create(
            number_in_table=value[0],
            order_number=value[1],
            price_in_dollars=value[2],
            date_of_shipping=value[3],
            price_in_rubles=value[4]
        )
        order.save()


@app.task
def periodic_messaging():
    """This task messages every user who started work with the bot stating all due orders
    """
    chats = Chat.objects.all()
    due_orders = select_due_orders()
    due_orders_message = []
    for order in due_orders:
        due_orders_message.append(f"Заказ #{order.order_number} на сумму {order.price_in_dollars} $ ({order.price_in_rubles} в рублях) должен придти {order.date_of_shipping}. Срок поставки прошел\n")
    if due_orders_message:
        for chat in chats:
            for message in due_orders_message:
                bot.send_message(chat.chat_id_tel, message)


@app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    """This function sets up the constant fetching of the data from Google Sheet
    """
    sender.add_periodic_task(crontab(minute=0, hour=9), periodic_messaging.s(), name="periodic messages")
    sender.add_periodic_task(5.0, save_sheet_in_the_db.s(), name='Fetch sheet data')
