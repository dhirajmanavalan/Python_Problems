# Problem 2 - Count Digits

num = 987654
count = 0

while num > 0:
    count += 1
    num = num // 10

print("Digits:", count)
