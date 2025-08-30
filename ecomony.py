

#Bank account system
class bank_acc:
    def __init__(self):
          self.balance = 0

    def update(self, new):
         print("setting balance")
         self.balance = new

#Bet select System
def bet_select(player):
      while True:
          print("Please enter your bet")
          print("You have "+ str(player.balance)+ " Gold")
          print()
          bet = input("Bet: ")
          try:
               if int(bet) > player.balance:
                    print()
                    print("Not enough money")
                    print()
                    continue
               if int(bet) < 1:
                    print()
                    print("Invaild Bet")
                    print()
                    continue
               else:
                    return int(bet)
                    break
          except:
               print()
               print("Please enter a number!")
               print()