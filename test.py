import random
print(random.gauss(5,1))
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
class fighter:
        #These allow functions to pass through as a vaild values
        def name(name):
            return name

        str = None
        spd = None
        

       

            

def fighter_menu():
    fighter1 = fighter
    fighter2 = fighter 
    print("1. "+fighter1.name(get_name()))
    print("2. "+fighter2.name(get_name()))
    print("Please select your fighter")

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
