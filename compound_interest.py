def ci(p, r, t, n):
    amount=p*(1+(r*n/100))**t
    ci=amount-p
    print("total amount: ", amount)
    print("compound interest: ", ci)
    
p=float(input("enter principal: "))
r=float(input("enter rate : "))
t=float(input("enter time(in years): "))
n=float(input("enter no. of times interst is compounded in a year: "))

ci(p, r, t, n)
    