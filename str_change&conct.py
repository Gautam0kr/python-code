word=input("Enter a word: ")
ch=input("Enter char you want to replace: ")
new_ch=input("Enter new char: ")

for i in range(len(word)):
    if word[i]==ch:
        new_word=word[:i]+new_ch+word[i+1:]
        break
    
print(f"New word : {new_word}")
print("concatinating both words: ", word+new_word)

#also it can do the same as above
"""new=word.replace(ch, new_ch)
print(new)"""