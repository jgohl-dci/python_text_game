################################################################################# Setup
from assets import house_img, stone_img, desert_img, well_img, death_img
import random

yes_no = ["yes", "no"]
directions = ["left", "right", "forward", "backward"]
water = 5

def moving(water):
    water -= 1
    if water >= 5:
        print('You feel more and more thirsty!')
    elif water >= 1:
        print('You have the feeling that you are about to die of thirst!')
    else:
        print('You die of thirst! MUAHAHAHAHA. Farewell', name)
        death_img()
        quit()
    return water

################################################################################ Introduction
name = input("What is your name, adventurer?\n")
name = name.capitalize()
print("Greetings, " + name + ". Let us go on a journey!")
print("You find yourself on the edge of a desert.")
print("Can you find your way back to civilization?\n")

# Beginning
response = ""
while response not in yes_no:
    response = input("Would you like to step further into the desert?\nyes/no\n")
    if response == "yes":
        print("You head further into the desert. The sun burns relentlessly on your head.\n")
    elif response == "no":
        print("You are not ready for this quest. Goodbye, " + name + ".")
        quit()
    else: 
        print("I didn't understand that.\n")

################################################################################## Part 1
response = ""
choice = ""
while response not in directions:
    desert_img()
    print("To your left, you see sand.")
    print("To your right, there is more sand.")
    print("There is a rock between the sand in front of you.")
    print("Behind you is the exit of the desert.\n")
    response = input("What direction do you move?\nleft/right/forward/backward\n")
    
    water = moving(water)
    
    if response == "left":
        print("You fall into a hole. Unable to climb out. Farewell, " + name + ".")
        death_img()
        quit()
    elif response == "right":
        print("You head deeper into the desert.\n")
        desert_img()
    elif response == "forward":
        print("You step closer to the rock. Curious but also frightened")
        stone_img()
        while choice not in yes_no:
            choice = input("Do you want to pick it up?\nyes/no\n")
            if choice == "yes":
                print("You find a bottle of water.\n")
                water += 2
            elif choice == "no":
                print("Afraid of Snakes? Ok go on.")
            else: 
                print("I didn't understand that.\n")
    elif response == "backward":
        print("You leave the desert. Goodbye, " + name + ".")
        quit()
    else:
        print("I didn't understand that.\n")


################################################################################## Part 2
response = ""
choice = ""
while response not in directions:
    print('\n', name, "what's next? You are going to die if you are not getting out of here!")
    print("To your left, you see sand.")
    print("To your right, there is more sand.")
    print("There is a lot of sand in front of you.")
    print("Behind you is even more sand. It looks like you got lost.\n")
    response = input("What direction do you move?\nleft/right/forward/backward\n")
    
    water = moving(water)
    
    if response == "left":
        print("You head to the left. Right in front of you is an old building out of stone")
        house_img()
    elif response == "right":
        print("You fall into a hole. Unable to climb out. Farewell, " + name + ".")
        death_img()
        quit()
    elif response == "forward":
        print("You head forward. In front of you is an old murky well.")
        well_img()
        print("The water inside looks disgusting. But you are thirsty.")
        while choice not in yes_no:
            choice = input("Do you want to drink it?\nyes/no\n")
            if choice == "yes":
                gonna_die = 0

                for i in range(10 + 1):
                    number = random.randrange(0, 2)
                    gonna_die = gonna_die + number

                if gonna_die >= 5:
                    print('You drink a little bit from the well and feel refreshed!')
                    water += 1
                else:
                    print('You drink a little bit from the well. After a while your stomach starts to grumble.')
                    print('Maybe it was a bad idea to drink this water.')
                    water -= 3
                
            elif choice == "no":
                print("Maybe better for your health.")
            else: 
                print("I didn't understand that.\n")
    elif response == "backward":
        print("XXXXXXX.")
    else:
        print("I didn't understand that.\n")



print('\nThank you', name, 'for playing my little game!')
print('You barely survived. Remaining Water:', water)
