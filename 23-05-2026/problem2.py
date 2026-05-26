# Problem 2 - Find Maximum Number

numbers = [23, 67, 12, 89, 45]

maximum = numbers[0]

for i in numbers:
    if i > maximum:
        maximum = i

print("Maximum Number:", maximum)
