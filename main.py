import json
import urllib.request
import time
from queue import Queue
from bank import Bank
from PredictorMa import PredictorMa
from PredictorAvg import AvgPredict

history=[]
type=input('Moving avg or Change Avg (M/C): ')
cur = input('enter crypto currency: ')
of_cur = input('official currency in your country ex: cad, usd, mxn: ')
url = f'https://api.coingecko.com/api/v3/simple/price?ids={cur}&vs_currencies={of_cur}'
cur_bal = float(input(f'how much would you be willing to invest? {of_cur} '))
if type=='C':
  h=input('history(separate with coma): ')#change this line later
  if h!='':
    h.split(',')
  for item in h:
    history.append(int(item))
# initialize components
your_bank = Bank(cur_bal)

predictorM = PredictorMa()
predictorC=AvgPredict(history)



while 1:
      # get latest price
      req = urllib.request.urlopen(url).read().decode()
      d = json.loads(req)
      last_price = d[cur][of_cur]
      if type=='M':
        
        print('\n')
        print('last price:', last_price)
    
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        print('time: ', current_time)
    
        signal = predictorM.get_signal(last_price)
        print('moving avg(3):', predictorM.cur_mov_avg)
        print(signal)
      
      elif type=='C':
        print('\n')
        print('last price:', last_price)
        print('change avg:',predictorC.change_avg)
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        print('time: ', current_time)
        signal=predictorC.give_signal(last_price)
        print('signal:',signal)
        
      if signal == 'sell':
        your_bank.sell(last_price)
      elif signal == 'buy':
        your_bank.buy(last_price)
        
  
      your_bank.print_bals()
      print('\n\n')

      time.sleep(15)
  
