# TUTORIAL DE ATACAR A UNA API EN PYTHON
# https://python.gotrained.com/python-json-api-tutorial/

import requests
import json

url = "https://api.exchangeratesapi.io/latest?symbols=USD,GBP"


response = requests.get(url)
data = response.text

parsed = json.loads(data)
date = parsed["date"]

gbp_rate = parsed["rates"]["GBP"]
usd_rate = parsed["rates"]["USD"]

print("On " + date + " EUR equals " + str(gbp_rate) + " GBP")
print("On " + date + " EUR equals " + str(usd_rate) + " USD")
