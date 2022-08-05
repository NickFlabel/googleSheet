import datetime
from .ExternalAPI.GoogleAPI import get_sheet
from .ExternalAPI.CBR_API import get_currency_rate
from .models import Sheet


def currency_converter(values, coversion_rate):
    """This function takes a list of orders and a conversion rate and adds a new column with price in rubles
    """
    for value in values:
        value.append(float(value[2]) * coversion_rate)
    return values


def correct_date_format(values):
    """This function corrects the data format given the list of formats of the sheet
    """
    for value in values:
        value[3] = datetime.datetime.strptime(value[3], '%d.%m.%Y').strftime('%Y-%m-%d')
    return values


def fetch_sheet():
    """This function gets the sheet data and performs necessary operations before saving the data to the db
    """
    values = get_sheet()
    rate = get_currency_rate()
    values = currency_converter(values, rate)
    values = correct_date_format(values)
    return values


def select_due_orders():
    """This function selects all due orders from the database
    """
    return Sheet.objects.filter(date_of_shipping__lte=datetime.date.today())