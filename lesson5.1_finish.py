import string
import keyword

name = input("my_task: ")

if not name:
    print(False)
elif name[0].isdigit():
    print(False)
elif name in keyword.kwlist:
    print(False)
elif name != name.lower():
    print(False)
elif any((ch in string.punctuation.replace("_", "")) or ch.isspace() for ch in name):
    print(False)
elif "__" in name:
    print(False)
elif name == "_":
    print(True)
elif name.startswith("__") and name.endswith("__"):
    print(False)
elif set(name) == {"_"}:
    print(False)
else:
    print(True)
