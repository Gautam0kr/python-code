prime=[]
def chkPrime(num):
    for i in range(2, num):
        if num%i==0:
            return
    else:
        prime.append(num)
        return
        
for i in range(3, 101):
    chkPrime(i)

print("Prime num between 1 to 100:")
for num in prime:
    print(num)