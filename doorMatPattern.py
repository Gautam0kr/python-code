temp=input().split()
n=int(temp[0])
m=int(temp[1])
k=(m-3)//2
l=1
for i in range((n-1)//2):
    print("-"*k, end="")
    print(".|."*l, end="")
    print("-"*k)
    k-=3
    l+=2

print("-"*((m-7)//2), end="")
print("WELCOME", end="")
print("-"*((m-7)//2))

x=k+3
y=l-2
for i in range((n-1)//2):
    print("-"*x, end="")
    print(".|."*y, end="")
    print("-"*x)
    x+=3
    y-=2