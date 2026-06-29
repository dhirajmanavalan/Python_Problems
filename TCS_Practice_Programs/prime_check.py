num = int(input())

if num<=1:
    print("No")
else:
    isprime = True

for i in range(2,num):
    if num%i==0:
        isprime = False
    else:
        isprime = True

if isprime:
    print("Prime")
else:
    print("No")