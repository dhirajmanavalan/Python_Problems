num = list(map(int, input().split()))

dupl = []

for i in num:
    if i not in dupl:
        dupl.append(i)

print(dupl)