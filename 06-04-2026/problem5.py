'''Longest Subarray with Sum = K'''
nums = [1, 2, 3, -2, 5]
k = 5

prefix_sum = 0
max_len = 0
seen = {}

for i in range(len(nums)):
    prefix_sum += nums[i]

    if prefix_sum == k:
        max_len = i + 1

    if (prefix_sum - k) in seen:
        max_len = max(max_len, i - seen[prefix_sum - k])

    if prefix_sum not in seen:
        seen[prefix_sum] = i

print("Max length:", max_len)