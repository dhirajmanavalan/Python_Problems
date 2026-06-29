n = list(map(int, input().split()))

duplicates = []

for i in n:
    if n.count(i)>1 and i not in duplicates:
        duplicates.append(i)

print(duplicates)

#
# arr = list(map(int, input().split()))
# duplicates = []
#
# for i in range(1, len(arr)):
#     for j in range(i+1, len(arr)):
#         if arr[i] == arr[j] and arr[i] not in duplicates:
#             duplicates.append(arr[i])
#
# print(duplicates)