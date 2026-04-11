'Merge K Sorted Lists (Using Heap)'
import heapq

lists = [[1,4,5],[1,3,4],[2,6]]

heap = []

for i in range(len(lists)):
    if lists[i]:
        heapq.heappush(heap, (lists[i][0], i, 0))

result = []

while heap:
    val, list_idx, ele_idx = heapq.heappop(heap)
    result.append(val)

    if ele_idx + 1 < len(lists[list_idx]):
        next_val = lists[list_idx][ele_idx + 1]
        heapq.heappush(heap, (next_val, list_idx, ele_idx + 1))

print(result)