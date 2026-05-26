# Problem 5 - Find Largest Digit

number = 983421

largest = 0

while number > 0:

    digit = number % 10

    if digit > largest:
        largest = digit

    number = number // 10

print("Largest Digit:", largest)
