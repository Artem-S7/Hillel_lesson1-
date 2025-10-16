import string

text = input("My task: ")

for ch in string.punctuation:
    text = text.replace(ch, "")

words = text.split()

words = [word.capitalize() for word in words]

hashtag = "#" + "".join(words)

if len(hashtag) > 140:
    hashtag = hashtag[:140]

print(hashtag)
