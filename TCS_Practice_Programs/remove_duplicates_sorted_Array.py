arr = list(map(int, input().split()))

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i]>arr[j]:
            arr[i],arr[j] = arr[j],arr[i]

print("Sorted: ",arr)

sort = arr
duplicates = []
print("Sorted array: ", sort)

for num in sort:
    if num not in duplicates:
        duplicates.append(num)
        print(duplicates)

print("Removing duplicates from sorted array: ",duplicates)


