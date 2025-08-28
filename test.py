import random

balance = 500
gameloop = True

#List of all names (TEMPORARY)
fighter_name = ["Joe", "Derek", "Edwin", "Donut-Eater", "Adrian", "Bart", "Xiang", "Melvin", "John", "Jerry", "Harry", "Chester", "Tom", "Andrew", "Jackson", "Mason", "Eugene", "Oswald", "Hobart", "Mortimer", "Reginald"]

#Chooses a random name from the list of names
def get_name():
        name = random.choice(fighter_name)
        return name

#Generates a random number from 0 to 10 for all atributes
def gen_atr():
      atr = random.randint(0,10)
      return atr


#This class contains every stat of the fighters
class Fighter:
     def __init__(self):
          self.name = get_name()
          self.str = gen_atr()
          self.spd = gen_atr()
          self.agi = gen_atr()
          self.con = gen_atr()
          self.int = gen_atr()
          self.size = gen_atr()

     def stat_check(self):
          print("Fighter's name is "+str(self.name))
          print("Strength = "+str(self.str))
          print("Speed = "+str(self.spd))
          print("Agilty = "+str(self.agi))
          print("Toughness = "+str(self.con))
          print("Intelligence = "+str(self.int))
          print("Size = "+str(self.size))    

def fighter_menu():
    fighter1 = Fighter()
    fighter2 = Fighter()
    print("1. "+fighter1.name)
    print("2. "+fighter2.name)
    print("Please select your fighter(1 or 2)")

def start():
    print("Welcome to Gambling Sim!.")
    print("In this game you will gamble on gladitors to earn money.")
    print("In order to begin you must chose one fighter and place a bet.")
    input("Press enter to continue")


def main_menu():
    print(balance)


while gameloop == True:
    fighter_menu()
    gameloop = False
