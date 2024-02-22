import random

random_number = random.randint(1, 100)

gusess_number = input("Guess between 1 and 100 :")

while int(gusess_number) != random_number:
    if int(gusess_number) < random_number:
        print("up")
        gusess_number = input("Guess between 1 and 100 :")
        continue
    elif int(gusess_number) > random_number:
        print("down")
        gusess_number = input("Guess between 1 and 100 :")
        continue
    else:
        print("correct")
        break
