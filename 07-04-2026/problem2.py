'Generate All Subsets (Power Set)'

nums = [1,2,3]
result = [[]]

for num in nums:
    new_subsets = []
    for subset in result:
        new_subsets.append(subset + [num])
    result += new_subsets

print(result)