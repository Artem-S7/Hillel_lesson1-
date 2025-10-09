#lesson 3

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
    result = x <= y
    print("x is less than y:", result)
elif operation == ">":
    result = x >= y
    print("x is greater than y!", result)

else:
    print("Error: unknown operation!")

print("Good job")

# lesonn 3.2

example = [2, 15, 0, 15, 777, 841, 14, 145,2025]

example.insert (0, example.pop())

print(example)

example = [123]

if len(example) <= 1:
    pass
else:
    example.insert(0, example.pop())

print(example)

#lesson 3.3

example = [12, 452, 3, 14, 115, 144]

if len(example) == 0:
    result = [[], []]

else:
    middle = (len(example) + 1) // 2
    first_part = example[:middle]
    second_part = example[middle:]
    result = [first_part, second_part]

print(result)