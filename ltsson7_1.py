def say_hi(name, age):
    return f"Hi. My name is {name} and I'm {age} years old"

say_hi("Alex", 32)
say_hi("Frank", 68)

rules1 = say_hi("Alex", 32)
rules2 = say_hi("Frank", 68)

print(rules1)
print(rules2)

assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", 'Test1'
assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'
print('ОК')