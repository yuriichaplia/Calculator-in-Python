from art import logo
print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {"+" : add,
              "-" : subtract,
              "*" : multiply,
              "/" : divide}

def calculator():
    should_continue = True
    first = float(input("What's the first number?: "))

    while should_continue:
        operator = str(input("+\n-\n*\n/\nPick an operation: "))
        second = float(input("What's the next number?: "))

        while operator == '/' and second == 0:
            second = float(input("While using division, second number cannot be 0. Enter a valid number: "))

        output = operations[operator](first, second)
        print(f"{first} {operator} {second} = {output}")
        action = input(f"Type 'y' to continue calculating with {output}," +
        " or type 'n' to start a new calculation: ").lower()

        if action == 'y':
            first = output
        else:
            should_continue = False
            print("\n" * 20)
            calculator()

calculator()
