arr = list(map(int,input().split()))

nums = []

for i in arr:
    if i != 0:
        nums.append(i)

zero = len(arr) - len(nums)

for i in range(zero):
    nums.append(0)

print(nums)