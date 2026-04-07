'''Next Greater Element (Right Side)'''
nums = [4, 5, 2, 25]
result = [-1] * len(nums)
stack = []

for i in range(len(nums)):
    while stack and nums[i] > nums[stack[-1]]:
        idx = stack.pop()
        result[idx] = nums[i]

    stack.append(i)

print(result)