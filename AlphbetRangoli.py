def print_rangoli(size):
    if size==0:
        return
    elif size==1:
        print("a")
        return
    s=2*size-2
    t=1
    for i in range(size-1):
        z=size
        print("-"*s, end="")
        for j in range(t):
            print(chr(z+96), end="-")
            z-=1
        z+=2
        for k in range(t-1):
            print(chr(z+96), end="-")
            z+=1
        print("-"*(s-1))
        t+=1
        s-=2
    
    for i in range(size, 0, -1):    
        print(chr(96+i), end="-")
    for i in range(98, size+96):
        print(chr(i), end="-") 
    print(chr(size+96))
    s+=2 
    t-=1       
    for i in range(size-1):
        z=size
        print("-"*s, end="")
        for j in range(t):
            print(chr(z+96), end="-")
            z-=1
        z+=2
        for k in range(t-1):
            print(chr(z+96), end="-")
            z+=1
        print("-"*(s-1))
        s+=2
        t-=1
        
        

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)