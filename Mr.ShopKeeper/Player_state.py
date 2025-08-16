
from config import *

class Player():
    def __init__(self, money = DEFAULT_MONEY, xp = DEFAULT_XP, level = DEFAULT_LEVEL, storage = DEFAULT_STORAGE):
        self._money = money
        self._xp = xp
        self._level = level
        self._storage = storage


    @property
    def money(self):
        return self._money

    @money.setter
    def money(self, value):
        self._money = value

    @property
    def xp(self):
        return self._xp

    @xp.setter
    def xp(self, value):
        self._xp = value

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value

    @propery
    def storage(self):
       return self._storage

    @storage.setter
    def storage(self, value):
        self._storage = value



    def earn_money(self, amount):
        self._money += amount
        print(f"You earned {self._money} €")

    def earn_xp(self, amount):
        self.xp += amount
        print(f"You earned {self.xp} xp")

    def earn_level(self, amount):
        self.level += amount
        print(f"You leveled up ! Your current level now: {self.level}")

    def earn_storage(self, amount):
        self.storage += amount
        print(f"You expanded your Shop storage. Your new Storage: {self.storage}")
    
    
