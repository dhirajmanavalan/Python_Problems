# Problem 5 - Print Fibonacci Series

first = 0
second = 1

print(first)
print(second)

for i in range(1, 9):

    next_number = first + second

    print(next_number)

    first = second
    second = next_number
