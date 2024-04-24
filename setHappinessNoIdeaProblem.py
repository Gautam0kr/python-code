temp=input()
Arr=set(map(int, input().split()))
A=set(map(int, input().split()))
B=set(map(int, input().split()))
happ=0
for n in Arr:
    if n in A:
        happ+=1
    elif n in B:
        happ-=1
print(happ)
    
