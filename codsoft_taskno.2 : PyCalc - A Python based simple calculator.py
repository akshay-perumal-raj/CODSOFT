print("PyCalc - A Python based simple calculator")

def inputfloat(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

a = inputfloat("\nEnter the first number: ")
b = inputfloat("Enter the second number: ")

while True:
    print("\nEnter the operation")
    print("Please enter")
    print("1 - if you want to perform addition")
    print("2 - if you want to perform subtraction")
    print("3 - if you want to perform multiplication")
    print("4 - if you want to perform division and obtain the quotient")
    print("5 - if you want to perform division and obtain the remainder")
    print("6 - if you want to perform floor division")
    print("7 - if you want to perform exponentiation", a, "raised to", b)
    print()
    
    try:
        op = int(input())
    except ValueError:
        print("Invalid input. Please enter a number from 1 to 7")
        continue

    print()

    if op == 1:
        print(a, "+", b, "=", a + b)
    elif op == 2:
        print(a, "-", b, "=", a - b)
    elif op == 3:
        print(a, "*", b, "=", a * b)
    elif op == 4:
        try:
            print(a, "/", b, "=", a / b)
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
    elif op == 5:
        print(a, "%", b, "=", a % b)
    elif op == 6:
        print(a, "//", b, "=", a // b)
    elif op == 7:
        print(a, "**", b, "=", a ** b)
    else:
        print("Please enter a number from 1 to 7")
        continue

    op2 = input("\nDo you want to perform another calculation? (yes/no): ").lower()
    if op2 != 'yes':
        print("Exiting the calculator. Goodbye!")
        break
