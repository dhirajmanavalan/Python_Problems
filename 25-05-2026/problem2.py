# Problem 2 - Find Sum of Digits

number = 5678

total = 0

while number > 0:

    digit = number % 10

    total = total + digit

    number = number // 10

print("Sum of Digits:", total)
