'Course Schedule (Cycle Detection in Graph)'
numCourses = 2
prerequisites = [[1,0]]

graph = {i: [] for i in range(numCourses)}

for a, b in prerequisites:
    graph[a].append(b)

visited = set()
path = set()

def dfs(node):
    if node in path:
        return False
    if node in visited:
        return True

    path.add(node)

    for nei in graph[node]:
        if not dfs(nei):
            return False

    path.remove(node)
    visited.add(node)
    return True

for course in range(numCourses):
    if not dfs(course):
        print("Cannot finish courses")
        break
else:
    print("Can finish courses")