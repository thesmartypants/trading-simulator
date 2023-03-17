class predict:
  def __init__(self,hisory):
    self.history=history
  def give_signal(self,price):
    self.history.append(price)
    his_avg=sum(self.history)/len(self.history)
    if his_avg>0:
      return 'buy'
    elif his_avg<0:
      return 'sell'
    else:
      return ''
