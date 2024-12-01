import random # we need this library
#sets score and number of chances to 0
score = 0
chance = 0
#game 1
#-----------------------------------------------------#
while chance <= 10: # the user has 10 turns
    dice = random.randint(1, 6) # this is the dice variable
    print(dice)
    choice = int(input("roll again = 1, keep = 0 ")) # allows the user to select weather or not to keep the current roll
    if choice == 0: # the user wants to keep the roll
        score = score + dice
        print("total is " + str(score) + "$")
        chance = chance + 1
    elif choice == 1: # the user want to roll again
        score = score + random.randint(1, 6)
        print("total is " + str(score) + "$")
        chance = chance + 1
#-----------------------------------------------------#

#game 2
#-----------------------------------------------------#
count = 0 # sets count to 0
choice = "y" # sets inital choice to yes (to roll the die the first time)
while choice != "N": # while not no (basically if the user wants to keep playing) 
    choice = input("keep going? Y or N ")
    count = count + random.randint(1, 6)
    print(count)
    if 0 != (count ** 0.5) % 1: # checks if the current total is not a perfect square
        continue
    count = 0
    print("you lose HAHAHA") # if the total is a perfect square the user will lose everything
    break
print("Your final score is " + str(count))
