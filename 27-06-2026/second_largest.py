# a = int(input())
#
# arr = list(map(int, input().split()))
#
# largest = float('-inf')
# second = float('-inf')
#
# for i in arr:
#     if i > largest:
#         second = largest
#         largest = i
#
#     elif i > second and i != largest:
#         second = i
#
# print("Largest: ", largest)
# print("Second: ", second)





a = int(input())

arr = list(map(int, input().split()))

largest = float('-inf')
second = float('-inf')

for i in arr:
    if i > largest:
        second = largest
        largest = i

    elif i > second and i != largest:
        second = i

print("Largest",largest)
print("Second_Largest", second)















