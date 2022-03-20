import os
clear = lambda: os.system('cls')

menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    'money': 0
}

cost = list()
selection = list()

def payment():
    print('\n''Please insert ${:,.2f} for your {}.'.format(cost[0],selection[0]))
    try:
        qu = int(input('\n'"Insert how many Quarters? "))
        qu_total = float(qu) * .25
    except ValueError:
        clear()
        print("Please insert valid coins. ")
        payment()
    try:
        di = int(input("Insert how many Dimes? "))
        di_total = float(di) * .10
    except ValueError:
        clear()
        print("Please insert valid coins. ")
        payment()
    try:
        ni = int(input("Insert how many Nickles? "))
        ni_total = float(ni) * .05
    except ValueError:
        clear()
        print("Please insert valid coins. ")
        payment()
    try:
        pe = int(input("Insert how many Pennies? "))
        pe_total = float(pe) * .01
    except ValueError:
        clear()
        print("Please insert valid coins. ")
        payment()
    total = (qu_total + di_total + ni_total + pe_total)
    change = total - cost[0]
    if change >= 0:
        profit = resources['money'] + cost[0]
        resources['money'] = profit
        if selection[0] == "Espresso":
            water = resources['water'] - 50
            coffee = resources['coffee'] - 18
            resources['water'] = water
            resources['coffee'] = coffee
        elif selection[0] == "Latte":
            water = resources['water'] - 200
            milk = resources['milk'] - 150
            coffee = resources['coffee'] - 24
            resources['water'] = water
            resources['milk'] = milk
            resources['coffee'] = coffee
        elif selection[0] == "Cappuccino":
            water = resources['water'] - 250
            milk = resources['milk'] - 100
            coffee = resources['coffee'] - 24
            resources['water'] = water
            resources['milk'] = milk
            resources['coffee'] = coffee
        print('\n'"Total inserted is ${:,.2f}, your change is {:,.2f}. Enjoy your {}!".format(total,change,selection[0]))
        input('Press Enter to return to Main Menu. ')
        main_menu()
    elif change < 0:
        print('\n'"Sorry that's not enough money. ${:,.2f} refunded.".format(total))
        input('\n''Press Enter to return to Main Menu. ')
        main_menu()



def espresso_chk():
    a = menu['espresso']['ingredients']['water']
    b = resources['water']
    c = menu['espresso']['ingredients']['coffee']
    d = resources['coffee']
    if a > b :
        print('\n' "Sorry there is not enough Water.")
        input('Press Enter to return to Main Menu. ')
        main_menu()
    elif c > d :
        print('\n' "Sorry there is not enough Coffee.")
        input('Press Enter to return to Main Menu. ')
        main_menu()
    else:
        cost.clear()
        selection.clear()
        cost.append(1.5)
        selection.append("Espresso")
        payment()


def latte_chk():
    a = menu['latte']['ingredients']['water']
    b = resources['water']
    c = menu['latte']['ingredients']['coffee']
    d = resources['coffee']
    e = menu['latte']['ingredients']['milk']
    f = resources['milk']
    if a > b :
        print('\n' "Sorry there is not enough Water.")
        input('Press Enter to return to Main Menu. ')
        main_menu()
    elif c > d :
        print('\n' "Sorry there is not enough Coffee.")
        input('Press Enter to return to Main Menu. ')
        main_menu()
    elif e > f:
        print('\n' "Sorry there is not enough Milk.")
        input('Press Enter to return to Main Menu. ')
        main_menu()
    else:
        cost.clear()
        selection.clear()
        cost.append(2.5)
        selection.append("Latte")
        payment()


def cappuccino_chk():
    a = menu['cappuccino']['ingredients']['water']
    b = resources['water']
    c = menu['cappuccino']['ingredients']['coffee']
    d = resources['coffee']
    e = menu['cappuccino']['ingredients']['milk']
    f = resources['milk']
    if a > b :
        print('\n' "Sorry there is not enough Water.")
        input('Press Enter to return to Main Menu. ')
        main_menu()
    elif c > d :
        print('\n' "Sorry there is not enough Coffee.")
        input('Press Enter to return to Main Menu. ')
        main_menu()
    elif e > f:
        print('\n' "Sorry there is not enough Milk.")
        input('Press Enter to return to Main Menu. ')
        main_menu()
    else:
        cost.clear()
        selection.clear()
        cost.append(3)
        selection.append("Cappuccino")
        payment()


def main_menu():
    clear()
    choice_a = input('What would you like?' '\n'
    '\n' '1. Espresso = $1.5' '\n' '2. Latte = $2.5' '\n'
    '3. Cappuccino = $3.0' '\n' '\n' 'Enter choices: ')
    choice_a = choice_a.lower()
    if choice_a == 'off' or choice_a == "quit":
        print('Turning off.')
        quit()
    elif choice_a == 'report':
        print('\n''Water: '+str(resources['water']))
        print('Milk: '+str(resources['milk']))
        print('Coffee: '+str(resources['coffee']))
        print('Money: $'+str(resources['money']))
        restock = input('\n''Would you like to restock resources? Enter "Yes" to restock: ')
        restock = restock.lower()
        if restock == "yes":
            resources['water'] = 300
            resources['milk'] = 200
            resources['coffee'] = 100
            input('\n'"Resources restocked. Press Enter to return to Main Menu. ")
        else:
            input('\n'"No change to resources. Press Enter to return to Main Menu. ")
        main_menu()
    elif choice_a == '1' or choice_a == "espresso":
        espresso_chk()
    elif choice_a == '2' or choice_a == 'latte':
        latte_chk()
    elif choice_a == '3' or choice_a == 'cappuccino':
        cappuccino_chk()
    else:
        input('\n''Invalid Choice. Press enter to choose again. ')
        main_menu()

main_menu()
