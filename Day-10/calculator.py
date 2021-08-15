from art import logo

print (logo)
# Caclculator

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract (n1, n2):
    return n1 - n2

# Multiply
def multiply (n1, n2):
    return n1 * n2

# Divide
def divide (n1, n2):
    return n1 / n2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}


symbol = ''
for signs in operations:
    symbol += signs + ", "
num1 = float(input("Enter the first number: "))

should_continue = True
while should_continue:
    print(f"Choose the one of the following: {symbol}")
    symbol_operation = input("Enter here: ")
    num2 = float(input("Enter the second numeber: "))
    function = operations[symbol_operation]
    answer = function(num1, num2)
    print(f"{num1} {symbol_operation} {num2} = {answer}")

    ask_continue = input('Do want to calculate more numbers? Type "Yes" or "No":' ).lower()
    if ask_continue == "yes":
        num1 = answer
    else: 
        should_continue = False
        print("Good Bye!")
