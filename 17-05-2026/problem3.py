# Problem 3 - Count Even Numbers

nums = [1, 2, 3, 4, 5, 6, 8]
count = 0

for n in nums:
    if n % 2 == 0:
        count += 1

print("Even Count:", count)
