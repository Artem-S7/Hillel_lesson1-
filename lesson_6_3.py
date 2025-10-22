num = int(input("Введіть число: "))

while num > 9:
    result = 1
    for d in str(num):
        result *= int(d)
    num = result

print(num)