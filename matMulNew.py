def create(m, n):
    mat=[]
    for i in range(m*n):
         mat.append(int(input()))
    return mat

def matmul(mat1, m, n, mat2, p, q):
    res=[]
    temp=0
    temp1=0
    r=temp1
    c=temp
   
    for i in range(m):
        for times in range(q):
            el=0
            temp=0
            for j in range(p):
                el+=(mat1[r]*mat2[c])  
                r+=1
                c+=q 
            r=temp1
            c=temp+1
            res.append(el)
        c=0
        temp1+=n
        r=temp1      
    return res

def print_mat(mat, m, n):
    el=0
    while el<m*n:
        for i in range(n):
            print(mat[el], end=" ")
            el+=1
        print()
        
print("Enter first matrix elements : ")        
mat1= create(2,3)
print()
print("mat1: " )
print_mat(mat1, 2, 3)
print()

print("Enter second matrix elements : ")
mat2= create(3,2)
print()
print("mat2:" )
print_mat(mat2, 3, 2)  
print()

print("Resultant matrix of mat1 and mat2 is : ") 
resultant=matmul(mat1, 2, 3, mat2, 3, 2)
print_mat(resultant, 2, 2)

            