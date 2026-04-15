'Minimum Window Substring'
s = "ADOBECODEBANC"
t = "ABC"

from collections import Counter

need = Counter(t)
have = {}
required = len(need)
formed = 0

l = 0
res = (float('inf'), 0, 0)

for r in range(len(s)):
    char = s[r]
    have[char] = have.get(char, 0) + 1

    if char in need and have[char] == need[char]:
        formed += 1

    while formed == required:
        if (r - l + 1) < res[0]:
            res = (r - l + 1, l, r)

        have[s[l]] -= 1
        if s[l] in need and have[s[l]] < need[s[l]]:
            formed -= 1

        l += 1

print("Min window:", s[res[1]:res[2]+1])