# Python program to convert the currency
# of one country to that of another country
# https://fixer.io/quickstart   ,get ur api key here
# http://data.fixer.io/api/latest?access_key=058de1a6ef7e99c4b3166be180c096ea
# Import the modules needed
import requests


class Currency_convertor:
    # empty dict to store the conversion rates
    rates = {}

    def __init__(self, url):
        data = requests.get(url).json()
        # print(data)

        # Extracting only the rates from the json data
        self.rates = data["rates"]

    # function to do a simple cross multiplication between
    # the amount and the conversion rates
    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount
        if from_currency != 'EUR':
            amount = amount / self.rates[from_currency]

        # limiting the precision to 2 decimal places
        amount = round(amount * self.rates[to_currency], 2)
        print('{} {} = {} {}'.format(initial_amount, from_currency, amount, to_currency))
        # print(f"{initial_amount} { from_currency} = {amount} {to_currency}")



# Driver code
if __name__ == "__main__":
    YOUR_ACCESS_KEY = '058de1a6ef7e99c4b3166be180c096ea'
    url = str.__add__('http://data.fixer.io/api/latest?access_key=', YOUR_ACCESS_KEY)
    # url = "http://data.fixer.io/api/latest?access_key=" + YOUR_ACCESS_KEY
    # print(url)
    c = Currency_convertor(url)
    from_country = input("From Country [BTC, INR, USD, AUD, ..etc ]: ").upper()
    to_country = input("TO Country [BTC, INR, USD, AUD, ..etc ]: ").upper()
    amount = int(input("Amount : "))

    c.convert(from_country, to_country, amount)