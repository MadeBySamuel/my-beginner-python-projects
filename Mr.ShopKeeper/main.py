
import time

from function import *

import config



def main():



    Selected = []
    print("Hi, welcome to my shopping cart game")

    print("First of all, I will let you choose the inital budget that you can use for your shop")
    time.sleep(4)
    print("You have 3 difficulty levels - three different amount of money")



    print("---------------------")
    for i in difficulty:
        print(f"{i['diff']:7} --- {i['money']:7}€")
    print("---------------------")

    while True:
        x = input("Choose your difficulty level: (easy, medium, hard) \n").lower()
        for i in difficulty:
            if i['diff'] == x:
                money = i['money']
                money_status(money)
                break
            else:
                print("Invalid difficulty level")
                continue

        if money > 0:
            break


    print("Now, that you choose your difficulty level")

    print("Lets begin")

    print("First you should start with district of your shop")
    print("You will start in Orava")
    showLocation()

    boolean = False
    while True:
        if boolean:
            break
        place = input("Choose one place where you will start your journey:")
        for i in Orava:
            if i['name_of_district'] == place:
                if i['status'] and money > i['price_of_district']:
                    print(f"Great you will {"start" if level == 0 else "continue"} with {place}")
                    money -= i['price_of_district']
                    money_status(money)
                    boolean = True
                    break
                elif i['status'] == False or money < i['price_of_district']:
                    if not i['status']:
                        print(f"Sorry but your level {level} is too low for this location")
                        break
                    else:
                        print("Sorry but you dont have enough money")
                        break

    print("Now that you chose your location it is time for you to choose in which type of shop you want to start: ")

    while True:

        print(f"Here you have {len(Listof)} types of groceries you can find in shop")

        for x in Listof:
            print("------------------")
            print(x)


        while True:
            def switch(choice):
                match choice:
                    case 'bakery':
                        showBakery()
                        Selected.append(bakery)
                        return bakery
                    case 'fruit':
                        showFruit()
                        Selected.append(Fruit)
                        return Fruit
                    case 'vegetable':
                        showVegetable()
                        Selected.append(Vegetable)
                        return Vegetable
                    case 'dairy':
                        showDairy()
                        Selected.append(Dairy)
                        return Dairy
                    case 'meat':
                        showMeat()
                        Selected.append(Meat)
                        return Meat
                    case 'pentry':
                        showPentry()
                        Selected.append(Pentry)
                        return Pentry

            try:
                choice = input("You can view the content of all different types of shops \n").lower()
                name= switch(choice)

                if choice != 'bakery' and choice != 'fruit' and choice != 'vegetable' and choice != 'dairy' and choice != 'meat' and choice != 'pentry':
                    print("Please enter a valid choice")
                    continue

            except ValueError:
                print("Please enter a valid choicem")
            else:
                yesno = input(f"Do you want to continue with this {choice} shop ? y/n \n ").lower()
                if yesno == 'y':
                    break
                elif yesno == 'n':
                    continue
                else:
                    print("Please enter a valid choice")
                    continue


        print(f"You also have a truck capacity of {truckcapacity} items")

        print(f"Now it is time to choose from your {choice} list")


        while True:
            found = 0
            for i in name:
                print(f"{i['name']:10} --- {i['quantity']:10} --- {i['capacity']:10} --- {i['price']:10}")
            while True:
                item = input("Which item you would like to buy: ")

                for i in name:
                    if i['name'] != item:
                        pass
                    else:
                        found =+1
                        break
                if found != 1:
                    print("Please enter a valid choice")
                else:
                    break

            amount = int(input(f"How much of {item} would you like to buy? "))
            for i in name:
                if i['name'] == item:
                    if amount > (i['capacity'] - i['quantity']) or amount > truckcapacity:
                        if amount > i['capacity'] - i['quantity']:
                            print(f"Sorry, you don't have enough capacity to buy {amount} {item}s")
                            print(f"Your capacity is {i['capacity']}")
                        else:
                            print(f"Sorry, you don't have enough truck capacity to buy {amount} {item}s")
                            print(f"Your truck capacity is {truckcapacity}")

                    else:
                        realmoney = money
                        money = money - i['price'] * amount
                        if money < 0:
                            money = realmoney
                            print(f"You dont have enough money to buy {amount} {item}s")
                        else:
                            truckcapacity -= amount
                            i['quantity'] += amount
                        break


            money_status(f"{money:.2f}")

            truck_capacity(truckcapacity)


            continuee = input("Do you want to continue? y/n \n").lower()
            if continuee == 'y':
                continue
            elif continuee == 'n':
                break
            else:
                print("Please enter a valid choice")



if __name__ == '__main__':
    main()

