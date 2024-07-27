#coffee machine

#%% start dictionary

MENU = {
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
    "money": 0
}


#%% function
def report():
    for kind, surplus in resources.items():
        if kind == 'money':
            print(f"{kind}: ${surplus}")
        else:
            print(f"{kind}: {surplus}ml")

def check_resources(choice,ingredients):
    for item in ingredients:
        if ingredients[item]>resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def make_coffee(choice, ingredients, bill):
    for item in ingredients:
        resources[item] -= ingredients[item]
    resources['money'] += MENU[choice]['cost']
    report()
    print(f"Here is your {choice}. Enjoy!")

def payment(cost):
    total = float(input(f'The price is {cost}, please insert your coins: '))  
    if total >= cost:
        change = total - cost
        if change > 0:
            print(f"Here is ${change:.2f} in change.")  
        return True  
    else:
        print('Sorry, that\'s not enough money. Money refunded.')
        return False 

#%%main loop

'''
在while True循环中，除break外无论发生什么循环都不会终止。
即，无论True or False，循环都会继续
'''
def main_program():

    while True:
        ask_question = input('What would you like? (espresso/latte/cappuccino):').lower() 

        if ask_question == 'report':
            report()

        elif ask_question == 'off':         #添加off终止程序
            break

        elif ask_question in ['espresso', 'latte', 'cappuccino']:
            choice = ask_question
            ingredients = MENU[choice]['ingredients']
            bill = MENU[choice]['cost']

            if check_resources(choice,ingredients):                #此处如果为False，循环会直接回到开头。
                if payment(bill):
                    make_coffee(choice,ingredients,bill)

        else:
            print("Invalid selection. Please choose from 'espresso', 'latte', 'cappuccino', or 'report'.")


main_program()


