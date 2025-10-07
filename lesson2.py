number = input("Enter a number: ")

a = int(number) // 1000
b = (int(number) // 100) % 10
c = (int(number) // 10) % 10
d = int(number) % 10

print(a)
print(b)
print(c)
print(d)



number = 98765

a = number // 10000
b = (number // 1000) % 10
c = (number // 100) % 10
d = (number // 10) % 10
e = number % 10

reversed_number = e * 10000 + d * 1000 + c * 100 + b * 10 + a

print(reversed_number)


