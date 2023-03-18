from PredictorAvg import AvgPredict
from PredictorMa import PredictorMa

Predictor1 = AvgPredict([1, 3, 6, 2, 4])
if Predictor1.give_signal(7) == 'buy':
  print('Avg predictor success')
else:
  print('Avg predictor failed')
Predictor2=PredictorMa()
Predictor2.get_signal(2)
Predictor2.get_signal(4)
if Predictor2.get_signal(7)=='sell':
  print('Moving avg predictor success')
else:
  print('Moving avg predictor failed')
