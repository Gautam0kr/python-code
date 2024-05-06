k, m=map(int, input().split())
max=[]
for _ in range(k):
    temp=list(map(int, input().split()))
    
    temp.pop(0)
   
    temp.sort()
    max.append(temp[-1])
res=0
for num in max:
    res+=(num ** 2)
print(res % m)
