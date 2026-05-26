# Problem 1 - Check Binary Number

num = "10101"

flag = True

for ch in num:
    if ch not in "01":
        flag = False

if flag:
    print("Binary Number")
else:
    print("Not Binary")
