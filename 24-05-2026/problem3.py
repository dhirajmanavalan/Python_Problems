# Problem 3 - Count Digits in Number

number = 987654

count = 0

while number > 0:

    number = number // 10

    count = count + 1

print("Digit Count:", count)
