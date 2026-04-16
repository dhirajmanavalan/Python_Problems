'Alien Dictionary (Topological Sort)'
from collections import defaultdict, deque

words = ["wrt","wrf","er","ett","rftt"]

graph = defaultdict(set)
indegree = {c:0 for word in words for c in word}

for w1, w2 in zip(words, words[1:]):
    for c1, c2 in zip(w1, w2):
        if c1 != c2:
            if c2 not in graph[c1]:
                graph[c1].add(c2)
                indegree[c2] += 1
            break

queue = deque([c for c in indegree if indegree[c] == 0])
result = ""

while queue:
    c = queue.popleft()
    result += c
    for nei in graph[c]:
        indegree[nei] -= 1
        if indegree[nei] == 0:
            queue.append(nei)

print("Order:", result)