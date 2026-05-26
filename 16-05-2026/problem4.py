# Problem 4 - Find Minimum Number

nums = [34, 11, 67, 2, 90]

smallest = nums[0]

for n in nums:
    if n < smallest:
        smallest = n

print("Smallest:", smallest)
