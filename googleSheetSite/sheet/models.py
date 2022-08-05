from django.db import models


# Create your models here.
class Sheet(models.Model):
    """This model represents information fetched from Google Sheets"""
    number_in_table = models.IntegerField()
    order_number = models.IntegerField()
    price_in_dollars = models.DecimalField(max_digits=40, decimal_places=2)
    date_of_shipping = models.DateField()
    price_in_rubles = models.DecimalField(max_digits=40, decimal_places=2)


class Chat(models.Model):
    """This model stores all active chats with the bot
    """
    chat_id_tel = models.IntegerField(unique=True)