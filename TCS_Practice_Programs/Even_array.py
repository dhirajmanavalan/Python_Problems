a = int(input())
arr = list(map(int, input().split()))

even_num = [x for x in arr if x%2==0]

print(even_num)