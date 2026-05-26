# Problem 4 - Count Vowels

text = "python programming"
count = 0

for ch in text:
    if ch in "aeiou":
        count += 1

print("Vowels:", count)
