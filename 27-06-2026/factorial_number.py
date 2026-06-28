n = int(input())
a = 1

if n<0:
    print("Negative number")

for i in range(1,n+1):
    a = a*i
    print(a)

print(a)
