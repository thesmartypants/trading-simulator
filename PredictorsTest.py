class AvgPredict:
  def __init__(self,history):
    self.history=history
  def give_signal(self,price):
    self.history.append(price)
    change_avg=0
    for i in range (len(self.history)):
      if i!=0:
        change_avg+=self.history[i]-self.history[i-1]
        
    change_avg=change_avg/len(self.history)
    if change_avg>0:
      return 'buy'
    elif change_avg<0:
      return 'sell'
    else:
      return ''
