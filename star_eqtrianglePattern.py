r=int(input("Enter num of rows: "))
i=1
j=r-2
while i<=r:
    while j>=0:
        print(end=" ")
        j-=1
    print(i*"* ")
    i+=1
    j=r-i-1
    
    
r=int(input("Enter num of rows: "))
i=1
j=r-2
k=1
while i<=r:
    while j>=0:
        print(end=" ")
        j-=1
    k=1
    while k <=i:
        print(k, end=" ")
        k+=1
    print()
    i+=1
    j=r-i-1
