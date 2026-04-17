'Union Find (Disjoint Set)'
parent = [i for i in range(5)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    parent[find(x)] = find(y)

union(0,1)
union(1,2)
union(3,4)

print("Connected (0,2):", find(0) == find(2))
print("Connected (0,4):", find(0) == find(4))