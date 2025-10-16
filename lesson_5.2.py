while True:
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))
    operation = input("Enter an operation (+, -, *, /, <, >): ")

    if operation == "+":
        result = x + y
        print("Result:", result)

    elif operation == "-":
        result = x - y
        print("Result:", result)

    elif operation == "*":
        result = x * y
        print("Result:", result)

    elif operation == "/":
        if y == 0:
            print("Error: division by zero is not allowed!")
        else:
            result = x / y
            print("Result:", result)

    elif operation == "<":
        result = x < y
        print("x is less than y:", result)

    elif operation == ">":
        result = x > y
        print("x is greater than y:", result)

    else:
        print("Error: unknown operation!")

    cont = input("Do you want to continue? (y/n): ").strip().lower()
    if cont != "y":
        print("Calculator stopped.")
        break

