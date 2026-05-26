# Problem 3 - Count Uppercase Letters

text = "PyThOn ProGraM"

count = 0

for ch in text:

    if ch.isupper():
        count = count + 1

print("Uppercase Letters:", count)
