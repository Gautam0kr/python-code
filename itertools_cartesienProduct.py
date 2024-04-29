from itertools import product
A=list(map(int, input().split()))
B=list(map(int, input().split()))
A.sort()
B.sort()
P=list(product(A, B))
for pair in P:
    print(pair, end=" ")
