# Problem 1 - Palindrome String

text = "madam"

reverse = ""

for ch in text:

    reverse = ch + reverse

if text == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")
