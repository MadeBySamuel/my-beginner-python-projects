
from config import *

class Player():
    def __init__(self, money = DEFAULT_MONEY, xp = DEFAULT_XP, level = DEFAULT_LEVEL, storage = DEFAULT_STORAGE):
        self.money = money
        self.xp = xp
        self.level = level
        self.storage = storage

    def earn_money(self, amount):
        self.money += amount
        print(f"You earned {self.money} ")

    def earn_xp(self, amount):
        self.xp += amount
        print(f"You earned {self.xp}")







player = Player()

player.earn_money(54)
