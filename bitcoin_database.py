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
import fsspec
import requests
import urllib3
import json

cred = credentials.Certificate("crypto-database-7f5d1-firebase-adminsdk-pr6ob-0e60267db9.json")
app = firebase_admin.initialize_app(cred)

ref = db.reference("/", url='https://bitcoin-realtime-database-default-rtdb.firebaseio.com/')
i = 1
coin_data_list = []

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
    'Coin Name' : 'Bitcoin',
    'Current Price' : current_price,
    'Market Cap' : market_cap,
    'Price Change' : price_change,
    'Price Volume' : price_volume,
    'Date' : current_date,
  }
  ref.push(coin_dict)
  time.sleep(60)

  
