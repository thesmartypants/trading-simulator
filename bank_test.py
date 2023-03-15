from bank import bank

bank1 = bank(100)
bank1.buy(2)
if bank1.investment_balance == 50 and bank1.balance == 0:
    print("buy works")
else: print("buy failed")  
  
#balance: 0
#invesment balance: 1
bank1.print_bals()
bank1.sell(2)
if bank1.investment_balance == 0 and bank1.balance == 100:
    print("sell works")
else: print("sell failed")
#100
#0
bank1.print_bals()