import random
import math
import ecomony as ecom

gameloop = True
player = ecom.bank_acc()
max_atr = 10

with open('names.txt', "r") as file:
     fighter_name = file.read().split()

#Chooses a random name from the list of names
def get_name():
        name = random.choice(fighter_name)
        return name

#Generates a random number from 0 to 10 for all atributes
def gen_atr():
      atr = random.randrange(0,max_atr,1)
      return atr

#This class contains every stat of the fighters
class Fighter:
     def __init__(self):
          name_count = 0
          self.name = get_name()
          self.str = gen_atr()
          self.spd = gen_atr()
          self.agi = gen_atr()
          self.con = gen_atr()
          self.int = gen_atr()
          self.size = gen_atr()
          self.pop = random.randrange(1,max_atr*10,1)
          self.atr_list = [self.str, self.spd, self.agi, self.con, self.int, self.size]
          self.avg = sum(self.atr_list)/len(self.atr_list)

          if self.int > max_atr * 0.8:
               if name_count == 0:
                    self.name = self.name + " The Wise"
                    name_count += 1
               else:
                    self.name = self.name + " and The Wise"

          if self.str > max_atr * 0.8:
               if name_count == 0:
                    self.name = self.name + " The Strong"
                    name_count += 1
               else:
                    self.name = self.name + " and The Strong"

          if self.spd > max_atr * 0.8:
               if name_count == 0:
                    self.name = self.name + " The Energetic"
                    name_count += 1
               else:
                    self.name = self.name + " and The Energetic"

          if self.size > max_atr * 0.8:
               if name_count == 0:
                    self.name = self.name + " The Imposing"
                    name_count += 1
               else:
                    self.name = self.name + " and The Imposing"

          if self.con > max_atr * 0.8:
               if name_count == 0:
                    self.name = self.name + " The Tough"
                    name_count += 1
               else:
                    self.name = self.name + " and The Tough"

          if self.agi > max_atr * 0.8:
               if name_count == 0:
                    self.name = self.name + " The Dexterous"
                    name_count += 1
               else:
                    self.name = self.name + " and The Dexterous"
          
          #Prints all atributes. Used for debugging
     def stat_check(self):
          print("Fighter's name is "+str(self.name))
          print("Strength = "+str(self.str))
          print("Speed = "+str(self.spd))
          print("Agilty = "+str(self.agi))
          print("Toughness = "+str(self.con))
          print("Intelligence = "+str(self.int))
          print("Size = "+str(self.size))   
          print("Popularity = "+str(self.pop)) 

def main_menu():
    print(player.balance)

def fighter_select(fighter1, fighter2):
     while True:
          print("1. "+fighter1.name)
          print("2. "+fighter2.name)
          sel_fighter = input("Please select your fighter(1 or 2)")
          if sel_fighter == "1":
               print()
               return fighter1
          if sel_fighter == "2":
               print()
               return fighter2
          if sel_fighter != "1" or "2":
               print()
               print("Please select vaild fighter!")
               print()

              

def fighter_menu():
    print()
    fighter1 = Fighter()
    fighter2 = Fighter()
    test = sum(fighter1.atr_list)/len(fighter1.atr_list)
    test2 = sum(fighter2.atr_list)/len(fighter2.atr_list)
    print(str(test))
    print(str(test2))
    chosen = fighter_select(fighter1,fighter2)

    print("You have selected "+ chosen.name)
    print(chosen.stat_check())
    bet = ecom.bet_select(player)
    print("You have bet "+ str(bet)+" gold on "+ chosen.name)
    player.update(player.balance - bet)
    if fighter1.avg > fighter2.avg:
         if fighter1 is chosen:
              player.update(player.balance + bet*2)
              print(fighter1.name+" Won the Battle")
              print("You won "+ str(bet*2))
              input("Press enter to contiune")     
              fighter_menu()
         else:
              print(fighter2.name+" Won")
              print("You lost "+ str(bet))
              input("Press enter to contiune")
              fighter_menu()     

    if fighter2.avg > fighter1.avg:
         if fighter2 is chosen:
              player.update(player.balance + bet*2)
              print(fighter2.name+" Won the Battle")
              print("You won "+ str(bet*2))
              input("Press enter to contiune")     
              fighter_menu()
         else:
              print(fighter1.name+" Won")
              print("You lost "+ str(bet))   
              input("Press enter to contiune") 
              fighter_menu()      

    else:
         print("Fighters are equal and kill eachother at the same\ntime in battle")
         print("Game tied, you lost nothing")     
         input("Press enter to contiune")
         fighter_menu()       


          
     
              
def start():
    player.update(500)
    print()
    print("Welcome to Gambling Sim!")
    print("In this game you will gamble on gladitors to earn money.")
    print("In order to begin you must chose one fighter and place a bet.")
    input("Press enter to continue")
    fighter_menu()



while gameloop == True:
    
    start()
    gameloop = False
