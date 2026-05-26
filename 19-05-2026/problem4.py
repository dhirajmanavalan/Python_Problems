# Problem 4 - Count Uppercase Letters

text = "PyThOn"

count = 0

for ch in text:
    if ch.isupper():
        count += 1

print("Uppercase:", count)
