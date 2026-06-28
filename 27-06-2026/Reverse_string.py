# s = input()
# print(s[::-1])

s = input()
rev = ""

for i in s:
    rev = i + rev
    print(rev)

print(rev)