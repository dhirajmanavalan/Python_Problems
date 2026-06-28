n = list(map(int, input().split()))

duplicates = []

for i in n:
    if n.count(i)>1 and i not in duplicates:
        duplicates.append(i)

print(duplicates)