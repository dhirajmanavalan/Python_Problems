num = int(input())

palindrome = num

rev = 0

while num > 0:
    digit = num%10
    rev = rev * 10 +digit
    num = num // 10

if palindrome == rev:
    print("Palindrome")
else:
    print("Not a Palindrome")