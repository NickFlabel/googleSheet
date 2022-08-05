from pycbrf import ExchangeRates


def get_currency_rate():
    """This functions gets the current USD to RUB exchange rate from the Central Bank of Russia
    """
    rates = ExchangeRates()
    return float(rates['USD'].rate)
