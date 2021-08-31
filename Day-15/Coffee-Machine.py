import data
on = True

water = data.resources['water']
milk = data.resources['milk']
coffee = data.resources['coffee']
money = 0

while on:

    # user input
    user_input = int(input('What would you like? 1.Espresso 2.Latte 3.Cappuccino): '))
    if user_input == 1:
        user_input = 'espresso'
    elif user_input == 2:
        user_input = 'latte'
    elif user_input == 3:
        user_input = 'cappuccino'

    # if user_input == 'off':
    #     on = False
    # elif user_input == 'report':
    #     print(f'Water: {water} \n Milk: {milk} \n Coffee: {coffee} \n Money: {money}')

    def drink(user_input):
        global money, milk, coffee, water, on

        if user_input == 'off':
            on = False
        elif user_input == 'report':
            print(f'Water: {water} \nMilk: {milk} \nCoffee: {coffee} \nMoney: {money}')
        elif user_input == 'espresso':
            cost = data.MENU['espresso']['cost']
            print(f"Please insert ${cost}")
            quarters = int(input("25¢: "))
            dimes = int(input("10¢: "))
            nickels = int(input("5¢: "))
            pennies = int(input("1¢: "))
            money_inserted = (quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + (pennies * 0.01)
            if water < data.MENU['espresso']['ingredients']['water'] or coffee < data.MENU['espresso']['ingredients']['coffee']:
                print("Sorry there is not enough ingredients")
            if money_inserted == cost:
                print(f"Your {user_input} is ready.")
                money += money_inserted
                water -= data.MENU[user_input]['ingredients']['water']
                coffee -= data.MENU[user_input]['ingredients']['coffee']
            if money_inserted < cost:
                print("Sorry that's not enough money.")
                print(f"Please take your ${money_inserted}.")
            if money_inserted > cost:
                print(f"Please take your refund of ${round(money_inserted - cost, 2)}.")
                print(f"Your {user_input} is ready.")
                money += money_inserted
                water -= data.MENU[user_input]['ingredients']['water']
                coffee -= data.MENU[user_input]['ingredients']['coffee']

        elif water < data.MENU[user_input]['ingredients']['water'] or coffee < data.MENU[user_input]['ingredients']['coffee'] or milk < data.MENU[user_input]['ingredients']['milk']:
            print("Sorry there is not enough ingredients")
        else:
            cost = data.MENU[user_input]['cost']
            print(f"Please insert ${cost}")
            quarters = int(input("25¢: "))
            dimes = int(input("10¢: "))
            nickels = int(input("5¢: "))
            pennies = int(input("1¢: "))
            money_inserted = (quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + (pennies * 0.01)

            if money_inserted == cost:
                print(f"Your {user_input} is ready.")
                money += money_inserted
                milk -= data.MENU[user_input]['ingredients']['milk']
                water -= data.MENU[user_input]['ingredients']['water']
                coffee -= data.MENU[user_input]['ingredients']['coffee']
            if money_inserted < cost:
                print("Sorry that's not enough money.")
                print(f"Please take your ${money_inserted}.")
            if money_inserted > cost:
                print(f"Please take your refund of ${round(money_inserted - cost, 2)}.")
                print(f"Your {user_input} is ready.")
                money += money_inserted
                milk -= data.MENU[user_input]['ingredients']['milk']
                water -= data.MENU[user_input]['ingredients']['water']
                coffee -= data.MENU[user_input]['ingredients']['coffee']

    drink(user_input)




