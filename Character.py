# imports
import random


class Character:
    def __init__(self):
        self.HP = 10
        self.DEF = 10
        self.AC = 10
        self.AT = 3
        self.LV = 1
        self.EXP = 0

    if self.EXP > 100:
        pass



    def Race(self, race):
        match race:
            case "Dragonborn" | "1":
                self.AT += 1
            case "Dwarf" | "2":
                self.DEF += 2
            case "Human" | "3":
                self.HP += 1
                self.DEF += 1
                self.AC += 1
                self.AT += 1
            case _:
                self.AC += 1


PC = Character()
PC.Race("3")
print(PC.HP)
