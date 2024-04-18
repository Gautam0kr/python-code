def mat_input():
    mat=[]
    m=int(input("enter rows of matrix: "))
    n=int(input("enter column of matrix: "))
    print("Enter elements of matrix :")
    for i in range(m):
        tempmat=[]
        for j in range(n):
            el=int(input())
            tempmat.append(el)
        mat.append(tempmat)
    return mat

def print_mat(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            print(mat[i][j], end="  ")
        print() 
    print()   

def mat_mul(mat1, mat2):
    res=[]
    if len(mat1[0])==len(mat2):
        for i in range(len(mat1)):
            tempmat=[]
            for j in range(len(mat2[0])):
                el=0
                for k in range(len(mat2)):
                    el+=mat1[i][k]*mat2[k][j]
                tempmat.append(el)
            res.append(tempmat)
        return res
    else:
        print("Matrix multiplication not possible!")
        return

print("Matrix multiplication:")
print()
print("Enter first matrix :")
mat1=mat_input()
print("First matrix: ")
print_mat(mat1)

print("NOTE: columns of first matrix should be equal to rows of second matrix")
print("Enter second matrix: ")
mat2=mat_input()
print("Second matrix: ")
print_mat(mat2)

print("Resultant matrix:")
res=mat_mul(mat1, mat2)
if len(mat1[0])==len(mat2):
    print_mat(res)


