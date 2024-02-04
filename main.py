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
}

money = 0

# todo 1 ask customer

order = input("what would you like to order :(espresso/latte/cappuccino)")


# todo 2 off to shut down
# if order == "off":
#     break

# todo 3 create def report
def print_report():
    print(f"water:{'water'} ml\n milk:{'milk'} ml\n coffee:{'coffee'}g \n {'money'}")
# todo 4 print money

# todo 5 check resource def??

def check_resource():
    # check order menu recipe then access the ingredient then compare with the menu recipe
    # access the number of ingredient correctly
    count_ingredients = len(MENU[order]["ingredients"])
    for i in count_ingredients:

      MENU[order]["ingredients"]
