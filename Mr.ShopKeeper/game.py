
import time

from signup import login


def menu():
    menus = {"Start", "Settings", "Quit"}
    while True:
        press = input("Press: ")
        if press == "Start":
            play()
        elif press == "Settings":
            pass
        elif press == "Quit":
            return 0
        else:
            print("Invalid input")


def play():

    difficulty = [
        {"diff": "easy", "money": 2500}, {"diff": "medium", "money": 1500}, {"diff": "hard", "money": 750},
    ]

    print("Welcome to Shopkeeper")
    time.sleep(1.5)
    print("First of all, I would like to thank you for giving chance for my game <3")
    time.sleep(2)

    while True:
        print("First things first, I want you to choose your own difficulty: ")

        for i in difficulty:
            print(f"{i['diff']} {i['money']}")

        x = input("Choose difficulty: ")
        for i in difficulty:
            if x == i['diff']:
                money = i['money']

                break

        if x != "easy" and x != "medium" and x != "hard":
            print("Invalid input")
            time.sleep(1)
            input("Press enter to continue")
            continue
        else:
            break



