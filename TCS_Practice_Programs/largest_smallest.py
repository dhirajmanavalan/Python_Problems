# arr = list(map(int, input().split()))
#
# print(max(arr), "Largest")
# print(min(arr), "Minimum")

n = int(input())

arr = list(map(int,input().split()))

large = arr[0]
small = arr[0]

for i in arr:
    if i > large:
        large = i

    elif i < small:
        small = i

print("Large", large)
print("Small", small)