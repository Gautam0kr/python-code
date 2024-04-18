fib=[]
print("Fibonacci sequence:")
n=int(input("Enter number of terms:"))
a=0
b=1
fib.append(a)
fib.append(b)
for i in range(n-2):
    c=a+b
    fib.append(c)
    a=b
    b=c
print("Fibonacci sequence upto ", n, " terms: ")    
for terms in fib:
    print(terms, end="  ")