c11=0
c12=0
c21=0
c22=0
def prob1(c0):
    global c11, c12
    if c0=="c1":
        c11+=1
        
    elif c0=="c2":
        c12+=1
        
        
def prob2(c0):
    global c21, c22
    if c0=="c1":
        c21+=1
        
    elif c0=="c2":
        c22+=1
    
        
print("You are given two coins c1 and c2")
c=input("select any one coin first(c1 or c2): ")
for _ in range(10):
    c0=input("Again select any coin(c1 or c2): ")
    if c=="c1":
        prob1(c0)
    elif c=="c2":
        prob2(c0)
    c=c0
print()

print("Desired matrix of probability of selecting next coin:")        
print("     c1    c2")
print("c1"," ", c11/10," ", c12/10)
print("c2"," ", c21/10," ", c22/10)
# print()
# print()
# print("Desired matrix of probability of getting head or tail on selected coin:")
# print("     c1    c2")
# print("c1"," ", c11/20," ", c12/20)
# print("c2"," ", c21/20," ", c22/20)