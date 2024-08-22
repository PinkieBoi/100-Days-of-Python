from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
menu = Menu()
cash_box = MoneyMachine()

running = True

while running:
    order = input(f"What would you like? ({menu.get_items()}) ")
    if order == "off":
        running = False
    elif order == "report":
        coffee_machine.report()
        cash_box.report()
    else:
        drink = menu.find_drink(order)
        if drink and coffee_machine.is_resource_sufficient(drink):
            print(f"{drink.name}: ${drink.cost}")
            if cash_box.make_payment(drink.cost):
                coffee_machine.make_coffee(drink)
