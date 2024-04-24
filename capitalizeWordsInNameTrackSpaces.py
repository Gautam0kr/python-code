def solve(s):
    temp=[]
    result=[]
    for char in s:
        temp.append(char)
   
    for i in range(len(temp)):
        if i==0:
            if temp[0]!=" ":
                result.append(str(temp[0]).capitalize())
            
        elif temp[i]!=" " and temp[i-1]==" ":
            result.append(str(temp[i]).capitalize())
        else:
            result.append(temp[i])
    return "".join(result)

if __name__ == '__main__':
    s = input()

    result = solve(s)
    print(result)
