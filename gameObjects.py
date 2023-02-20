import random


class Dobbelsteen:
    def D4():
        return random.randint(0, 4)

    def D6():
        return random.randint(0, 6)

    def D8():
        return random.randint(0, 8)

    def D10():
        return random.randint(0, 10)

    def D12():
        return random.randint(0, 12)

    def D20():
        return random.randint(0, 20)

    def DN(n):
        return random.randint(0, n)


class Hero:
    def __init__(self, name):
        self.name = name

    AT = 2
    AC = 5
    DEF = 5

    def HeroInfo(self):
        print(
            f"Currently you have a Attack (AT) of {self.AT} and a Defence (DEF)of {self.DEF}")

    def Training(self):
        print(Dobbelsteen.D6())
        dobbelsteenrol = Dobbelsteen.D6()
        if dobbelsteenrol >= 1:
            self.AT += 1
        else:
            print("Je probeerde maar miste. De training haalde niets uit")
