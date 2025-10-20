numer = int(input("Введіть своє число: "))

days, remainder = divmod(numer, 86400)
hours, remainder = divmod(remainder, 3600)
minutes, seconds = divmod(remainder, 60)

if hours < 10:
    hours = "0" + str(hours)
else:
    hours = str(hours)

if minutes < 10:
    minutes = "0" + str(minutes)
else:
    minutes = str(minutes)

if seconds < 10:
    seconds = "0" + str(seconds)
else:
    seconds = str(seconds)

if days == 1:
    word = "day"
elif 2 <= days <= 4:
    word = "days"
else:
    word = "days"

print(str(days) + " " + word + ", " + hours + ":" + minutes + ":" + seconds)


