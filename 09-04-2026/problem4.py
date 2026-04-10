'Merge Two Sorted Lists'
l1 = [1,2,4]
l2 = [1,3,4]

i = j = 0
result = []

while i < len(l1) and j < len(l2):
    if l1[i] < l2[j]:
        result.append(l1[i])
        i += 1
    else:
        result.append(l2[j])
        j += 1

result.extend(l1[i:])
result.extend(l2[j:])

print(result)