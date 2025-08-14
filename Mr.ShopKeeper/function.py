


from list import *
from location import *
import config

def truck_capacity():
    print(f"Truck Capacity: {config.truckCapacity}")

def money_status():
    print(f"Money Status: {config.money}")




def shop(money):
    priced = 0
    print("Welcome to the upgeade shop")

    money_status(money)
    while True:
        for i in List:
            print(f"{i['name']}: {i['price']}")
            priced = i['price']
            print(f"Level: {i['level']}")
        if money < 800:
            print("You don't have enough money")
            pressq = input("Press q to quit")
            if pressq == "q":
                break
            else:
                print("Please enter q to quit")
        else:
            choosen = input(f"Do you want to upgrade your Truck capacity for {priced} € ? ")
            if choosen == "yes":
                money -= priced
                for i in List:
                    i['level'] += 1

        print("Do you want to upgrade again ? ")
## -- treba pokracovat


def header():
    print("------------------------------------------------------------------------------------------")
    print(f"name          quantity/maximum amount          price         Shopping budget {config.money}€    ")
    print("------------------------------------------------------------------------------------------")


def showBakery():
    print("List of things that Bakery sells")
    header()
    for i in bakery:
        print(f"{i['name']:10} --- {i['quantity']:10} --- {i['capacity']:10} --- {i['price']:10}")


def showFruit():
    print("List of things that Fruit shop sells")
    header()
    for i in Fruit:
        print(f"{i['name']:10} --- {i['quantity']:10} --- {i['capacity']:10} --- {i['price']:10}")


def showVegetable():
    print("List of things that shop with Vegatable sells")
    header()
    for i in Vegetable:
        print(f"{i['name']:10} --- {i['quantity']:10} --- {i['capacity']:10} --- {i['price']:10}")


def showDairy():
    print("List of things that Dairy shop sells")
    header()
    for i in Dairy:
        print(f"{i['name']:10} --- {i['quantity']:10} --- {i['capacity']:10} --- {i['price']:10}")


def showMeat():
    print("List of things that Meat shop sells")
    header()
    for i in Meat:
        print(f"{i['name']:10} --- {i['quantity']:10} --- {i['capacity']:10} --- {i['price']:10}")



def showPentry():
    print("List of things that Meat shop sells")
    header()
    for i in Meat:
        print(f"{i['name']:10} --- {i['quantity']:10} --- {i['capacity']:10} --- {i['price']:10}")


def showLocation():
    print("Orava")
    counter = 1
    print(f"       Miesto ---     Cena za pozemok ---   Level --- ")
    print("-----------------------------------------------------------------------------------------------")
    for i in Orava :
        print(f"{counter}. --- {i['name_of_district']:12} --- {i['price_of_district']:7}€ --- {i['level']:10} --- {"Odomknutá časť" if i['status'] == 1 else "Zamknutá časť":10}")
        counter += 1


