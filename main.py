import json
import urllib.request
import time
from queue import Queue
from bank import Bank
from predictorma import PredictorMa

cur = input('enter crypto currency: ')
of_cur = input('official currency in your country ex: cad, usd, mxn: ')
url = f'https://api.coingecko.com/api/v3/simple/price?ids={cur}&vs_currencies={of_cur}'
cur_bal = float(input(f'how much would you be willing to invest? {of_cur} '))
# initialize components
your_bank = Bank(cur_bal)

predictor = PredictorMa()

while 1:
    # get the latest price
    req = urllib.request.urlopen(url).read().decode()
    d = json.loads(req)
    last_price = d[cur][of_cur]
    print('\n')
    print('moving avg prediction: '+str(predictor.cur_mov_avg))
    print('last price:', last_price)

    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print('time: ', current_time)

    signal = predictor.get_signal(last_price)
    print('moving avg(3):', predictor.cur_mov_avg)
    print(signal)
    if signal == 'sell':
        your_bank.sell(last_price)
    elif signal == 'buy':
        your_bank.buy(last_price)

    your_bank.print_bals()
    print('\n\n')

    time.sleep(15)
