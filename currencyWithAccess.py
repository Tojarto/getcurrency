import requests
import json
import os

if  os.path.isfile('token.txt') :
    print ('Leyendo credenciales del archivo token.txt')
    token = open('token.txt','r+').read().rstrip("\n").rstrip("\r")
elif 'CURRENCYTOKEN' in os.environ :
    print('Leyendo variables de entorno')
    token = os.environ["CURRENCYTOKEN"]
else:
    print('El archivo no existe')
    raise IOError

url = "http://data.fixer.io/api/latest?access_key=" + token

response = requests.get(url)
data = response.text
parsed = json.loads(data)
date = parsed["date"]

gbp_rate = parsed["rates"]["GBP"]
usd_rate = parsed["rates"]["USD"]
print("On " + date + " EUR equals " + str(gbp_rate) + " GBP")
print("On " + date + " EUR equals " + str(usd_rate) + " USD")
