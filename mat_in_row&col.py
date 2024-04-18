m=int(input("Enter num of row of matrix: "))
n=int(input("Enter num of col of matrix: "))
print("Enter elements of matrix: ")
mat=[]
for i in range(m):
    row=[]
    for j in range(n):
        el=int(input())
        row.append(el)
    mat.append(row)
    
print("Matrix in one row: ")
for el in mat:
    for i in range(n):
        print(el[i], end="  ")
    
print()
print("Matrix in one col: ")
for el in mat:
    for i in range(n):
        print(el[i])
        
#also we can create a new mat or list for row and col and print them
'''print()
print("Matrix in one row:")
rowmat=[]
for i in range(len(mat)):
    for j in range(len(mat[0])):
        el=mat[i][j]
        rowmat.append(el)
for el in rowmat:
    print(el, end="  ")

print()
print("Matrix in one col: ")
for el in rowmat:
    print(el)'''