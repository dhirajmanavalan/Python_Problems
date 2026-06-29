num = int(input())
power = len(str(num))
total = 0

temp = num

while num >0:
    digit = num % 10
    total = total+digit ** power
    num = num // 10

if total == temp :
    print("Armstrong")
else:
    print("No")