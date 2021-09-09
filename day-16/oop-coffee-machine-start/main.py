from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money = MoneyMachine()
coffee_maker = CoffeeMaker()
is_on = True

while is_on:
    option = menu.get_items()
    user_choice = input(f"What would you like to order? {option}: ")

    if user_choice == "off":
        is_on = False
    elif user_choice == "report":
        coffee_maker.report()
        money.report()
    else:
        drink = menu.find_drink(user_choice)
        is_enough_resource = coffee_maker.is_resource_sufficient(drink)
        if is_enough_resource:
            is_enough_money = money.make_payment(drink.cost)
            if is_enough_money:
                coffee_maker.make_coffee(drink)
        else:
            print("Sorry, you run out of stock for today!!")
            is_on = False
