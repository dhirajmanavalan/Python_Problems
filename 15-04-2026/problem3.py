'Shortest Path in Weighted Graph'
import heapq

graph = {
    0: [(1,4),(2,1)],
    1: [(3,1)],
    2: [(1,2),(3,5)],
    3: []
}

dist = {node: float('inf') for node in graph}
dist[0] = 0

heap = [(0, 0)]

while heap:
    d, node = heapq.heappop(heap)

    if d > dist[node]:
        continue

    for nei, weight in graph[node]:
        if dist[node] + weight < dist[nei]:
            dist[nei] = dist[node] + weight
            heapq.heappush(heap, (dist[nei], nei))

print("Shortest distances:", dist)