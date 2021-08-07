import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json
import requests
import pandas as pd
import datetime as dt
import time
import json
import openpyxl

cred = credentials.Certificate("crypto-database-7f5d1-firebase-adminsdk-pr6ob-0e60267db9.json")
app = firebase_admin.initialize_app(cred)

ref = db.reference("/", url='https://crypto-database-7f5d1-default-rtdb.firebaseio.com/')
print(ref.get())
i = 1
coin_data_list = []
'''

while True:
  print(i)
  r = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true')
  response = r.json()
  current_price = response['bitcoin']['usd']
  market_cap = response['bitcoin']['usd_market_cap']
  price_change = response['bitcoin']["usd_24h_change"]
  price_volume = response['bitcoin']['usd_24h_vol']
  current_date = dt.datetime.now()

  coin_dict = {
    'Index' : i,
    'Coin Name' : 'Bitcoin',
    'Current Price' : current_price,
    'Market Cap' : market_cap,
    'Price Change' : price_change,
    'Price Volume' : price_volume,
    'Date' : current_date,
  }
  coin_data_list.append(coin_dict)
  i = i+1
  coin_df = pd.DataFrame(coin_data_list)
  data=json.dumps(json.loads(coin_df.to_json(orient='records')))
  ref.set(data)
  print(data)
  time.sleep(5)
'''