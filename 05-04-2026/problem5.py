'''Subarray Sum Equals K'''
nums = [1, 2, 3]
k = 3

count = 0
prefix_sum = 0
seen = {0: 1}

for num in nums:
    prefix_sum += num

    if (prefix_sum - k) in seen:
        count += seen[prefix_sum - k]

    seen[prefix_sum] = seen.get(prefix_sum, 0) + 1

print("Subarrays count:", count)