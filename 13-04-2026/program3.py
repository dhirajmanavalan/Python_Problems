'Word Ladder (Shortest Transformation)'
from collections import deque

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

wordSet = set(wordList)
queue = deque([(beginWord, 1)])

while queue:
    word, steps = queue.popleft()

    if word == endWord:
        print("Steps:", steps)
        break

    for i in range(len(word)):
        for c in "abcdefghijklmnopqrstuvwxyz":
            new_word = word[:i] + c + word[i+1:]
            if new_word in wordSet:
                queue.append((new_word, steps + 1))
                wordSet.remove(new_word)