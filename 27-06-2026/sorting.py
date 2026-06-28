# num = list(map(int,input().split()))
# num.sort(reverse=True)
#
# print(num)

num = list(map(int,input().split()))

for i in range(len(num)):
    for j in range(i+1,len(num)):
        if num[i] > num[j]:
            num[i],num[j]=num[j],num[i]

print(num)