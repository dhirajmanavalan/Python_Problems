# Problem 1 - Check Prime Number

number = 17

count = 0

for i in range(1, number + 1):

    if number % i == 0:
        count = count + 1

if count == 2:
    print("Prime Number")
else:
    print("Not Prime Number")
