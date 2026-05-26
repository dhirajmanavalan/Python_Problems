# Problem 5 - Find Smallest Digit

num = 52831
smallest = 9

while num > 0:
    digit = num % 10

    if digit < smallest:
        smallest = digit

    num = num // 10

print("Smallest Digit:", smallest)
