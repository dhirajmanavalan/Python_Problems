'''Find Missing Number (0 to n)'''
nums = [3, 0, 1]

n = len(nums)
expected_sum = n * (n + 1) // 2
actual_sum = sum(nums)

print("Missing number:", expected_sum - actual_sum)