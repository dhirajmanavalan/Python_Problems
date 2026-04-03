'''Two Sum Problem'''
nums = [2, 7, 11, 15]
target = 9

seen = {}

for i in range(len(nums)):
    diff = target - nums[i]

    if diff in seen:
        print("Indices:", seen[diff], i)
        break

    seen[nums[i]] = i