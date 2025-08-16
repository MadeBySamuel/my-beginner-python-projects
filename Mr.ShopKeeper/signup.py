import time
from shlex import split

import utils

import re

from login import Login


def check(string, letter):
    if string.find(letter) == -1:
        return False
    else:
        return True


def login():

    print("Hello :)")
    time.sleep(1)
    print("I am your botPete")
    time.sleep(1)
    username = input("What is your name? ")
    login = Login(username,email = "", password="")
    print("Welcome " + login.username)
    time.sleep(1)
    print(login.username + " please enter your game login credentials")
    while True:

        login.email = input("Enter Email for creating account to the game: ")

        pattern = r'^[a-zA-Z0-9._%+-]+@(gmail\.com|yahoo.com|outlook.com|hotmail.com|centrum.sk)$' # idk what does this thing do, I stole it from chatgpt

        if re.match(pattern, login.email):
            print(f"Ok so your email is {login.email} ")
            break
        else:
            print("Invalid email")
            if check(login.email, "@") and check(login.email, ".") == False:
                print("Email does not contain @ and . symbol")
            elif not check(login.email, "@"):
                print("Email does not contain @")
            else:
                print("Email does not contain .")

    time.sleep(1)
    print(f"Now it is time for your password.")
    time.sleep(1)
    print(f"Remember that your password has to be at least 8 characters long.")
    time.sleep(1)
    print(f"Furthermore, it must contain small letters, big letters, at least one number.")
    time.sleep(1)

    while True:
        login.password = input("Enter your password: ")
        big_letter_count = 0
        number_count = 0

        lenght_of_password = len(login.password)

        for x in login.password:
            if x.isupper():
                big_letter_count = 1
            if x.isdigit():
                number_count = 1

        if big_letter_count == 1 and number_count == 1:
            print("Your password is set")
            break
        elif big_letter_count != number_count:
            if big_letter_count == 1:
                print("Your password does not contain any numbers")
            else:
                print("Your password does not contain any big letters")







if __name__ == "__main__":
    login()





