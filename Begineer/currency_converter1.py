# currency converter
# using inbuilt functions

from forex_python.converter import CurrencyRates
c = CurrencyRates()
amount = int(input("Enter the amount : "))
from_currency = input("From Currency : [INR, USD, AUD, ..etc ] : ").upper()
to_currency = input("To Currency : [INR, USD, AUD, ..etc ] : ").upper()
print(from_currency, " To ", to_currency, amount)
result = c.convert(from_currency, to_currency, amount)
print(result)
