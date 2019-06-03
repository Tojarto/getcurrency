import requests
import json

url = "https://api.exchangeratesapi.io/latest?base=USD"

response = requests.get(url)
data = response.text
parsed = json.loads(data)
date = parsed["date"]
print("Date:", date, "\n")

rates = parsed["rates"]

for currency, rate in rates.items():
    print("USD =",currency, rate)
