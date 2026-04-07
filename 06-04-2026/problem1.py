'''Find All Duplicates in Array'''
nums = [4,3,2,7,8,2,3,1]
result = []

for num in nums:
    index = abs(num) - 1

    if nums[index] < 0:
        result.append(abs(num))
    else:
        nums[index] *= -1

print("Duplicates:", result)