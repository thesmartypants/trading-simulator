from PredictorAvg import AvgPredict

Predictor = AvgPredict([1, 3, 6, 2, 4])
if Predictor.give_signal(7) == 'buy':
  print('success')
