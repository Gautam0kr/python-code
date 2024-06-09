s=input()
count=1
for i in range(len(s)):
    if i+1==len(s):
        print("("+str(count)+",", str(s[i])+")")
        break
    if s[i]==s[i+1]:
        count+=1
        if i+1==len(s):
             print("("+str(count)+",", str(s[i])+")")
             break
    
    else:
        print("("+str(count)+",", str(s[i])+")", end=" ")
        count=1
        
        
# #using groupby
# from itertools import groupby
# s=input()
# for c, templist in groupby(s):
#     print(f'({len(list(templist))}, {c})', end=" ")