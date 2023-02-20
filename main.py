# imports
import random
import gameObjects


# vars
currentMode = ""

# code
print("Welcome to my testproject")

name = input("Please state your name: ")

hero = gameObjects.Hero(name)

print(
    f"Ah, There your are {hero.name}.")

hero.HeroInfo()


print("Do you wish to \n (T) train or \n (E) explore?")
while (currentMode != "T" and currentMode != "E"):
    currentMode = input()
    match currentMode:
        case "T":
            currentMode = "Training"
            hero.Training()
            hero.HeroInfo()
            break
        case "E":
            currentMode = "Exploring"

            break
        case _:
            print("Wrong input, please try again")
