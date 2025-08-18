from xml.sax.handler import property_encoding

from config import *


class BankAccount:
    def __init__(self, money):
        self.money = money

    @property
    def balance(self):
        return self.money

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("You cannot add negative amounts of money")
        else:
            self.money += amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("You cannot withdraw negative amounts of money")
        if self.money <= amount:
            raise ValueError("You don't have enough money")
        else:
            self.money -= amount




class Login:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

class Player():
    def __init__(self, login, bankaccount, xp = DEFAULT_XP, level = DEFAULT_LEVEL, storage = DEFAULT_STORAGE):
        self.BankAccount = bankaccount
        self.Login = login
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

    @property
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
        self._storage += amount
        print(f"You expanded your Shop storage. Your new Storage: {self._storage}")
    
 # player = Player(Login) <--
