from data import MENU
from data import resources
from data import coins

profit = 0


def check_resource(ingredients):
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Insufficient {item}.")
            return False
    return True


def calculate_coin():
    print("Please insert coins.")
    total = int(input("How many quarter?: ")) * coins["quarter"]
    total += int(input("How many dime?: ")) * coins["dime"]
    total += int(input("How many nickel?: ")) * coins["nickel"]
    total += int(input("How many penny?: ")) * coins["penny"]
    return total


def successful_payment(cost, collect_money):
    if collect_money >= cost:
        changes = round((collect_money - cost), 0)
        print(f"Here your changes ${changes}")
        global profit
        profit += cost
        return True
    else:
        print("You need to pay more!!")
        return False


def make_drink(choice, ordered_drink):
    for item in ordered_drink:
        resources[item] -= ordered_drink[item]
    print(f"Please enjoy your {choice}!!")


is_on = True

while is_on:
    user_choice = input("What would you like to order? (espresso/latte/cappuccino): ").lower()

    if user_choice == "off":
        is_on = False
    elif user_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Profit: ${profit}")
    else:
        drink = MENU[user_choice]
        if check_resource(drink["ingredients"]):
            payment = calculate_coin()
            if successful_payment(drink["cost"], payment):
                make_drink(user_choice, drink["ingredients"])
