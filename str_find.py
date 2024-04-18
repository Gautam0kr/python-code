word=str(input("Enter a word:"))
tempstr=str(input("Enter what you want to find: "))
if tempstr in word:
    print(f"{tempstr} is found in {word}")
else:
    print(f"{tempstr} is not found in {word}")