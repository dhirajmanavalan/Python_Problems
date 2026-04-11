'Word Break (DP)'
s = "leetcode"
wordDict = ["leet", "code"]

dp = [False] * (len(s) + 1)
dp[0] = True

for i in range(1, len(s) + 1):
    for word in wordDict:
        if i >= len(word) and dp[i - len(word)]:
            if s[i-len(word):i] == word:
                dp[i] = True

print("Can break:", dp[-1])