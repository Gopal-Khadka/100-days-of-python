from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_money_machine=MoneyMachine()
my_coffee_maker=CoffeeMaker()
menu=Menu()
is_on=True


my_money_machine.report()
my_coffee_maker.report()

while is_on:
    options=menu.get_items()
    choice=input(f"What would you like to have? {options}: ")
    if choice=="off":
        is_on=False
    elif choice=="report":
        my_money_machine.report()
        my_coffee_maker.report()
    else:
        drink=menu.find_drink(choice)
        if my_money_machine.make_payment(drink.cost) and my_coffee_maker.is_resource_sufficient(drink):
            my_coffee_maker.make_coffee(drink)
