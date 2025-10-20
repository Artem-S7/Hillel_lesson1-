import string

letters = string.ascii_letters

start, end = input("Введіть дві літери через дефіс: ").split("-")

start_index = letters.index(start)
end_index = letters.index(end)

if start_index > end_index:
    start_index, end_index = end_index, start_index

print(letters[start_index:end_index + 1])


