'''Sum of Even Numbers (1 to N)'''

n = int(input("Enter number: "))
total = 0

for i in range(1, n+1):
    if i % 2 == 0:
        total += i

print("Sum of even numbers:", total)



