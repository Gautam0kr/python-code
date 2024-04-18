fib=[0, 1]
print("Fibonacci sequence:")
n=int(input("Enter number of terms: "))
for i in range(n-2):
    next_term=fib[i]+fib[i+1]
    fib.append(next_term)
print(f"Fibonacci sequence upto {n} terms:")
for term in fib:
    print(term, end="  ")