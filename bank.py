# simulation for a bank account
class bank:

  def __init__(self,balance):
    self.balance=balance
    self.investment_balance=0
    
  def buy(self,price):
    if not self.balance == 0:  
      self.investment_balance = self.balance / price
      self.balance = 0

  def sell(self,price):
    if not self.investment_balance==0:
      self.balance = self.investment_balance * price
      self.investment_balance = 0

  def print_bals(self):
    print(f'balance: {self.balance}')
    print(f'investment balance: {self.investment_balance}')
