def si(p, r, t):
    si=p*r*t/100
    print("Simple interest : ", si)
    
p=float(input("Enter principal: "))
r=float(input("Enter rate: "))
t=float(input("Enter time: "))
si(p, r, t)