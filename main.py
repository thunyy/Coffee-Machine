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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# Function to check if operating
def operating(order):
    return order != "off"

# Function to check resources
def check_resource(order):
    for each_ingredient in MENU[order]["ingredients"]:
        if resources[each_ingredient] < MENU[order]["ingredients"][each_ingredient]:
            print(f"Sorry, there is not enough {each_ingredient}.")
            return False
    return True

# Function to make coffee
def coffee_making(order):
    for i in MENU[order]["ingredients"]:
        resources[i] -= MENU[order]["ingredients"][i]

# Process coins
def process_coin(order):
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01

    if total >= MENU[order]["cost"]:
        global profit
        profit += MENU[order]["cost"]
        change = round(total - MENU[order]["cost"], 2)
        print(f"Here is ${change} in change.")
    else:
        print("Sorry, that's not enough money. Money refunded.")
        exit()

# Main loop
while True:
    order = input("What would you like to order? (espresso/latte/cappuccino): ").lower()

    if not operating(order):
        break

    if order == "report":
        print(f"Water: {resources['water']} ml\nMilk: {resources['milk']} ml\nCoffee: {resources['coffee']}g\nMoney: ${profit}")
    elif check_resource(order):
        process_coin(order)
        coffee_making(order)
        print(f"Here is your {order}, enjoy!")
