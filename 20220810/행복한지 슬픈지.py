emoticon = input()

up = emoticon.count(":-)")
down = emoticon.count(":-(")

if up > down:
    print("happy")
elif down > up:
    print("sad")
elif up != 0 and down != 0 and up == down:
    print("unsure")
else:
    print("none")