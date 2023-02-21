# imports
import random
import gameObjects

# vars
currentMode = ""

# code
print("Welcome to my testproject")
name = input("Please state your name: ")
heroInstance = gameObjects.Hero(name)
Actions = gameObjects.Actions
print(
    f"Ah, There your are {heroInstance.name}.")
heroInstance.Info()


Actions.Fight(heroInstance, gameObjects.Enemy.Goblin)

Actions.Healing(heroInstance)
for i in range(0, 100, 1):
    Actions.Training(heroInstance)

Actions.Fight(heroInstance, gameObjects.Enemy.Goblin)


'''
gameLoop = True
while gameLoop:
    print("Do you wish to \n (T) train \n (E) explore \n (H) Healing \n (Q) Quit")
    while (currentMode != "T" and currentMode != "E"):
        currentMode = input()
        match currentMode:
            case "T":
                currentMode = "Training"
                Actions.Training(heroInstance)
                heroInstance.Info()
                break
            case "E":
                currentMode = "Exploring"
                Actions.Explore(heroInstance)
                break
            case "H":
                Actions.Healing(heroInstance)
                break
            case "Q":
                gameLoop = False
                break
            case _:
                print("Wrong input, please try again")
'''
print("Thanks for playing")
