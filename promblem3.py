def takeInput():
    a = float(input("Enter number 1\n "))
    b = float(input("Enter number 2\n "))
    operator = input("Enter the operator (+, -, *, /): ")
    return a, b, operator

def displayResult():
    a, b, operator = takeInput()
    #for the addition of two number
    if operator == "+":
        result = a + b
        print(f"{a} + {b} = {result}")
        #for substraction of two number
    elif operator == "-":
        result = a - b
        print(f"{a} - {b} = {result}")
        #for multiplication of two numbers
    elif operator == "*":
        result = a * b
        print(f"{a} * {b} = {result}")
        #for division of two number
    elif operator == "/":
        result = a / b
        print(f"{a} / {b} = {result}")
    else:
        print("Invalid operator entered")

displayResult()