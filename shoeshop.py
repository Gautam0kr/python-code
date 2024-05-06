#this program does not use counter
from collections import Counter
X=int(input()) #no. of shoes
S=list(map(int, input().split()))  #sizes of shoes
N=int(input()) #no. of customer
C=[]
for _ in range(N):
    C.append(list(map(int, input().split())))  #size and price
am=0
for i in range(N):
    if C[i][0] in S:
        am+=C[i][1]
        S.remove(C[i][0])
print(am)



# #using Counter
# from collections import Counter

# input()  # Useless info - ...the number of shoes.
# shoes = Counter(map(int, input().split()))
# customers = int(input())

# income = 0
# for customer in range(customers):  # Can replace 'customer' with _ since it is not used.
#     size, price = map(int, input().split())
#     if shoes[size]:
#         income += price
#         shoes[size] -= 1

# print(income)