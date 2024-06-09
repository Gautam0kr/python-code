from itertools import permutations
S, k=input().split()
Res=list(permutations(S, int(k)))
for el in Res:
    print("".join(el))
      
      
      
      
      
      
      
      