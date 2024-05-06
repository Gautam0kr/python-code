#input no. of words then all words.. print how many unique words and count same words
from collections import Counter
n=int(input())
words=[]
for _ in range(n):
    word=input()
    words.append(word)
s=Counter(words)
print(len(s))
for i in s.values():
    print(i, end=" ")
