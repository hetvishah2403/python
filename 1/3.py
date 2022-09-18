# Day 3 Project
#Treasure Island Game

print("Welcome to treasure island")
lor = input("You are at a crossroad,where do you wanna go? left or right?").lower()
if(lor=="right"):
    print("You fell! Game Over")
else:
    swim = input("Swim or wait?").lower()

    if(swim == "wait"):
        door = input("Which door? blue,yellow or red?")
        if(door == "blue" or door=="red"):
            print("Game Over")
        else:
            print("you win")

    else:
        print("Game Over")
        