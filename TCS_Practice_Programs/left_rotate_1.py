arr = list(map(int, input().split()))

temp = arr[0]

for i in range(len(arr) - 1):
    arr[i] = arr[i + 1]

arr[-1] = temp

print(arr)