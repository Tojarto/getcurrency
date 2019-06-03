import requests
import json

bases = ["USD", "EUR", "GBP"]

for base in bases:
    url = "https://api.exchangeratesapi.io/latest?base=" + base

    response = requests.get(url)
    data = response.text
    parsed = json.loads(data)

    rates = parsed["rates"]

    print("--------------- Rates in", base, "---------------")
    for currency, rate in rates.items():
        print(base, "=", currency, rate)
