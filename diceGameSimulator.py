import random
score = 0
chance = 0

while chance <= 10:
    dice = random.randint(1, 6)
    print(dice)
    choice = int(input("roll again = 1, keep = 0 "))
    if choice == 0:
        score = score + dice
        print("total is " + str(score) + "$")
        chance = chance + 1
    elif choice == 1:
        score = score + random.randint(1, 6)
        print("total is " + str(score) + "$")
        chance = chance + 1

count = 0
choice = "y"
while choice != "N":
    choice = input("keep going? Y or N ")
    count = count + random.randint(1, 6)
    print(count)
    if 0 != (count ** 0.5) % 1:
        continue
    count = 0
    print("you lose HAHAHA")
    break
print("Your final score is " + str(count))