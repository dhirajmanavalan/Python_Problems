'''Valid Anagram'''
s = "anagram"
t = "nagaram"

if sorted(s) == sorted(t):
    print("Valid Anagram")
else:
    print("Not Anagram")