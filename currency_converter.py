# currency conversion logic 


# is_valid_currency_code function checks if a given currency code is valid by using the forex-python module's CurrencyCodes class. The convert_currency function performs the currency conversion using the CurrencyRates class.from forex_python.converter import CurrencyRates, CurrencyCodes

from forex_python.converter import CurrencyRates, CurrencyCodes

# def is_valid_currency_code(currency_code):
#     currency_codes = CurrencyCodes()
#     return currency_codes.get_currency_name(currency_code) is not None

# def convert_currency(from_currency, to_currency, amount):
#     c = CurrencyRates()
#     return c.convert(from_currency, to_currency, amount)

def validate_currency_code(currency_code):
    currency_codes = CurrencyCodes()
    return currency_codes.get_currency_name(currency_code) is not None

def validate_amount(amount):
    try:
        float(amount)
        return True
    except ValueError:
        return False

def convert_currency(from_currency, to_currency, amount):
    currency_rates = CurrencyRates()
    converted_amount = currency_rates.convert(from_currency, to_currency, amount)
    currency_codes = CurrencyCodes()
    symbol = currency_codes.get_symbol(to_currency)
    converted_amount = round(converted_amount, 2)
    return f"{symbol} {converted_amount}"