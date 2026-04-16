'Find Median in Data Stream (Two Heaps)'
import heapq

nums = [5, 15, 1, 3]

small = []  # max heap (invert values)
large = []  # min heap

for num in nums:
    heapq.heappush(small, -num)
    heapq.heappush(large, -heapq.heappop(small))

    if len(large) > len(small):
        heapq.heappush(small, -heapq.heappop(large))

    if len(small) > len(large):
        median = -small[0]
    else:
        median = (-small[0] + large[0]) / 2

    print("Median:", median)