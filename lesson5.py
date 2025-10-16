import string
import keyword

name = input("my_task: ")

if not name:
    print(False)
elif name[0].isdigit():
    print(False)
elif name in keyword.kwlist:
    print(False)
elif not name.islower():
    print(False)
elif any(ch in string.punctuation.replace("_", "") or ch.isspace() for ch in name):
    print(False)
else:
    print(True)

