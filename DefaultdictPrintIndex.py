from collections import defaultdict
n,  m = map(int, input().split())
dic=defaultdict(list)
for _ in range(n):
    a=input()
    dic["A"].append(a)
for _ in range(m):
    b=input()
    dic["B"].append(b)
    
print(dic)

for char in dic["B"]:
    found=False
    for i in range(0, n) :
        
        if dic["A"][i]==char:
            print(i+1, end=" ")
            found=True
        elif found==True:
            continue
        else:
            print(-1, end="")
            break
    print()
    
