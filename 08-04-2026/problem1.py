'Top K Frequent Elements'
nums = [1,1,1,2,2,3]
k = 2

freq = {}

for num in nums:
    freq[num] = freq.get(num, 0) + 1

sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)

result = [item[0] for item in sorted_items[:k]]

print("Top K elements:", result)
