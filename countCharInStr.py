
S=input()
temp=list(S)
char=[]
count=[]
for c in temp:
    if c not in char:
        char.append(c)
for c in char:
    found=0
    for ch in temp:
        if c==ch:
            found+=1
    count.append(found)

for i in range(len(char)):
    print("("+str(count[i])+",", str(char[i])+")", end=" ")
