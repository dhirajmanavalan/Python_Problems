# Problem 4 - Count Vowels

text = "python programming language"

count = 0

for ch in text:

    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
        count = count + 1

print("Vowel Count:", count)
