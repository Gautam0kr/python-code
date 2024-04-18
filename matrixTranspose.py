def mat_input():
    mat=[]
    m=int(input("Enter rows of matrix: "))
    n=int(input("Enter columns of matrix: "))
    print("Enter elements of matrix: ")
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
    
def mat_transpose(mat):
    transpose=[]
    for i in range(len(mat[0])):
        tempmat=[]
        for j in range(len(mat)):
            el=mat[j][i]
            tempmat.append(el)
        transpose.append(tempmat)
    return transpose
            
print("Transpose of a matrix: ")
mat=mat_input()
print()
print("Entered matrix:")
print_mat(mat)
transpose=mat_transpose(mat)
print("Transposed matrix:")
print_mat(transpose)                
                       
                       
                       
                       
                       
                       
    