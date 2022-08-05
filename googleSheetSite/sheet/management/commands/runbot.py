from django.core.management.base import BaseCommand
from ...telegram_bot import bot


class Command(BaseCommand):
    """This command starts telegram bot
    """
    help = 'Starts telegram bot'

    def handle(self, *args, **options):
        bot.polling(none_stop=True, interval=1)