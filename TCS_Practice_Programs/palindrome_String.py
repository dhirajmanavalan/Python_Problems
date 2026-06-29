# s = input()
#
# if s == s[::-1]:
#     print("Palindrome")
# else:
#     print('Not palindrome')

s = input()

rev = ""

for i in s:
    rev = i + rev

if s == rev:
    print("palindrome == ", s)
else:
    print("No")


    