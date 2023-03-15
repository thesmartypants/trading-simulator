import json
import urllib.request
import time
from queue import queue
from bank import bank

cur = input('enter crypto currency: ')
of_cur = input('official currency in your country ex: cad, usd, mxn: ')
url = f'https://api.coingecko.com/api/v3/simple/price?ids={cur}&vs_currencies={of_cur}'
prices = queue(3)
cur_bal=float(input(f'how much would you be willing to invest? {of_cur} '))

your_bank=bank(cur_bal)

while 1:
  req = urllib.request.urlopen(url).read().decode()
  d = json.loads(req)
  last_price = d[cur][of_cur]

  prices.add(last_price)
  moving_avg_last3 = prices.get_avg()

  
  print('last price:', last_price)
  print('moving avg(3):', moving_avg_last3)
  t = time.localtime()
  current_time = time.strftime("%H:%M:%S", t)
  print('time: ', current_time)
  
  if not prices.is_ready():
    print('We dont know yet, the real moving avarage only shows up after the third cycle.')
  elif last_price > moving_avg_last3:
    print('sell')
    your_bank.sell(last_price)
  elif last_price < moving_avg_last3:
    print('buy')
    your_bank.buy(last_price)
  your_bank.print_bals()
  print('\n\n')

  time.sleep(10)
