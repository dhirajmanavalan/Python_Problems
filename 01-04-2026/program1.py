'''Check Divisible by 5 and 11'''

num = int(input("Enter number: "))

if num % 5 == 0 and num % 11 == 0:
    print("Divisible by both 5 and 11")
else:
    print("Not divisible by both")