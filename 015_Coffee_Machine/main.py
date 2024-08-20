import art
import coffee_data


def user_prompt():
    selection = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if selection == "off":
        exit()
    else:
        return selection


def display_report(resources):
    print(f"Water: {resources['water']}ml\nCoffee: {resources['coffee']}g\nMilk: {resources['milk']}ml"
          f"\nMoney: ${resources['money']}\n(Enter topup to replenish)")
    pass


def has_resources(drink, available_res):
    if drink["water"] > available_res['water']:
        print("Sorry there is not enough water.")
        return False
    elif drink['coffee'] > available_res['coffee']:
        print("Sorry there is not enough coffee.")
        return False
    elif drink['milk'] > available_res['milk']:
        print("Sorry there is not enough milk.")
        return False
    else:
        return True


def add_resources(resources):
    display_report(resources)
    new_resources = resources
    item = input("What would you like to replenish? ")
    amount = float(input("How much would you like to add (do not include units): "))
    new_resources[item] += amount
    return new_resources


def payment(cost):
    print("You can pay in Quarters (25c), Dimes (10c), Nickels (5c) and pennies (1c)")
    quarters = int(input("How many quarters: ")) * 0.25
    dimes = int(input("How many dimes: ")) * 0.1
    nickels = int(input("How many nickels: ")) * 0.05
    pennies = int(input("How many pennies: ")) * 0.01
    return cost - quarters + dimes + nickels + pennies


def make_coffee(resources, drink):
    new_resources = resources
    for item in drink:
        new_resources[item] -= drink[item]
    return new_resources


def coffee_machine():
    print(art.logo)
    running = True
    current_resources = coffee_data.resources
    available = coffee_data.coffees
    while running:
        drink = user_prompt()
        if drink == "topup":
            current_resources = add_resources(current_resources)
        elif drink == "report":
            display_report(current_resources)
        else:
            if has_resources(available[drink]['resources'], current_resources):
                # TODO: process coins
                print(f"{drink.capitalize()} is ${round(available[drink]['cost'], 2)}")
                paid = payment(available[drink]['cost'])
                if paid <= 0:
                    current_resources['money'] += available[drink]['cost']
                    if paid < 0:
                        print(f"Here is ${round(abs(paid), 2)} in change.")
                    # TODO: transaction success
                    current_resources = make_coffee(current_resources, available[drink]['resources'])
                    print(f"Dispensing {drink}. Enjoy!")
                else:
                    print("Sorry, that's not enough money. Money refunded.")
            else:
                print("Unable to dispense drink. Check resource report.")


coffee_machine()

