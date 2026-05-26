# Problem 2 - Find Smallest Number

numbers = [45, 12, 67, 3, 89]

smallest = numbers[0]

for i in numbers:

    if i < smallest:
        smallest = i

print("Smallest Number:", smallest)
