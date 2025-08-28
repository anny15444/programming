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
          name_count = 0
          self.name = get_name()
          self.str = gen_atr()
          self.spd = gen_atr()
          self.agi = gen_atr()
          self.con = gen_atr()
          self.int = gen_atr()
          self.size = gen_atr()

          if self.int > 8:
               if name_count == 0:
                    self.name = self.name + " The Wise"
                    name_count += 1
               else:
                    self.name = self.name + " and The Wise"

          if self.str > 8:
               if name_count == 0:
                    self.name = self.name + " The Strong"
                    name_count += 1
               else:
                    self.name = self.name + " and The Strong"

          if self.spd > 8:
               if name_count == 0:
                    self.name = self.name + " The Energetic"
                    name_count += 1
               else:
                    self.name = self.name + " and The Energetic"
          
          #Prints all atributes. Used for debugging
     def stat_check(self):
          print("Fighter's name is "+str(self.name))
          print("Strength = "+str(self.str))
          print("Speed = "+str(self.spd))
          print("Agilty = "+str(self.agi))
          print("Toughness = "+str(self.con))
          print("Intelligence = "+str(self.int))
          print("Size = "+str(self.size))    

def main_menu():
    print(balance)



#BIG ISSUES HERE
def fighter_select(fighter1, fighter2):
     sel_fighter = input("Please select your fighter(1 or 2)")
     if sel_fighter == "1":
         print()
         confirm = input("you have selected "+fighter1.name+"?  (Y [Yes] N [No])")
# IGNORED IF STATMENTS
         if confirm == "n" or "N":
               print("test")
               fighter_select(fighter1, fighter2)
         elif confirm == "y" or "Y":
               print("WIP")
               print(confirm)
               return fighter1
         

               
     

def fighter_menu():
    print()
    fighter1 = Fighter()
    fighter2 = Fighter()
    print("1. "+fighter1.name)
    print("2. "+fighter2.name)
    print()
    chosen = fighter_select(fighter1, fighter2)
    print(chosen.name)
    print(chosen.stat_check())

          
     
              
def start():
    print()
    print("Welcome to Gambling Sim!")
    print("In this game you will gamble on gladitors to earn money.")
    print("In order to begin you must chose one fighter and place a bet.")
    input("Press enter to continue")
    fighter_menu()



while gameloop == True:
    start()
    gameloop = False
