# lesson 4.1
numbers: list[int] = [0, 12, 71, 0, 0, 11, 14, 0, 17, 100, 0, 32.1]

non_zero = [num for num in numbers if num != 0]

result = non_zero + [0] * (len(numbers) - len(non_zero))

print(numbers)
print(result)

#lesson 4.2
numbers = [0, 12, 71, 0, 0, 11, 14, 0, 17, 100, 0, 32]

if numbers:
    result = sum(numbers[::2]) * numbers[-1]
else:
    result = 0

print(numbers)
print(result)

#lesson 4.3
import random

my_list = [random.randint(0, 100) for i in range(random.randint(3, 10))]
print(my_list)
print(sum(my_list))

print("Good job")