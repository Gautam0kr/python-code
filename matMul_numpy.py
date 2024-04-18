import numpy as np
def inputMat():
    m=int(input("Enter num of rows: "))
    n=int(input("Enter num of col: "))
    mat=[]
    print("Enter elements of matrix: ")
    for i in range(m):
        row=[]
        for j in range(n):
            el=int(input())
            row.append(el)
        mat.append(row)
    return mat

print("first matrix: ")
mat1=np.array(inputMat())
print("second matrix: ")
mat2=np.array(inputMat())
print()
print("Entered first matrix: ")
print(mat1)
print()
print("Entered second matrix: ")
print(mat2)
print()
print("Resultant matrix: ")
res=np.dot(mat1, mat2)
print(res)
