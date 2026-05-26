# Problem 4 - Armstrong Number

number = 153

temp = number

total = 0

while number > 0:

    digit = number % 10

    cube = digit * digit * digit

    total = total + cube

    number = number // 10

if temp == total:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
