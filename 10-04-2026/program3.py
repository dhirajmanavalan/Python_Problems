'Combination Sum (Backtracking)'
candidates = [2,3,6,7]
target = 7

result = []

def backtrack(start, path, total):
    if total == target:
        result.append(path)
        return
    if total > target:
        return

    for i in range(start, len(candidates)):
        backtrack(i, path + [candidates[i]], total + candidates[i])

backtrack(0, [], 0)

print(result)