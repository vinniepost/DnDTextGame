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


class Enemy:
    class Goblin:
        HP = 5
        AT = 1
        AC = 1
        DEF = 3


class Hero:
    def __init__(self, name):
        self.name = name
    HP = 10
    AT = 10
    AC = 5  # not used yet
    DEF = 10

    def CurrentHealth(self):
        print(f"You currently have {self.HP} Health left")

    def Info(self):
        print(
            f"Currently you have a Attack (AT) of {self.AT} and a Defence (DEF)of {self.DEF}")
        Hero.CurrentHealth(self)


class Actions:
    def Healing(hero):
        hero.HP = 10
        print(f"You've healed yourself back to {hero.HP} health")

    def Explore(hero):  # currently level 1?
        Actions.Fight(hero, Enemy.Goblin)

    def Fight(hero, enemy):  # Currently can lose but not win? enemy wins ?
        winner = ""
        while (hero.HP > 0 and enemy.HP > 0):
            if hero.AT > enemy.DEF:
                enemy.HP = enemy.HP - hero.AT
            elif enemy.AT > hero.DEF:
                hero.HP = hero.HP - enemy.AT
            if hero.HP <= 0:
                winner = "Hero wins!"
            if enemy.HP <= 0:
                winner = "Enemy Wins :( )"

        print(winner)

    def Training(hero):
        print(Dobbelsteen.D6())
        dobbelsteenrol = Dobbelsteen.D6()
        if dobbelsteenrol >= 1:
            hero.AT += 1
            print(
                f"Je training lukte en je AT is gestegen! Current: {hero.AT}")
        else:
            print("Je probeerde maar miste. De training haalde niets uit")
