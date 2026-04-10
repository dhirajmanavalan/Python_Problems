'House Robber'
nums = [2,7,9,3,1]

prev, curr = 0, 0

for num in nums:
    temp = max(curr, prev + num)
    prev = curr
    curr = temp

print("Max loot:", curr)