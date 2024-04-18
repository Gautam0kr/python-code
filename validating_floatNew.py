t=int(input())
def val_float(n):
    count=0
    con1=False
    con2=False
    if len(n)==1:
        return False
    for i in range(1,len(n)):
        if n[i]=="+" or n[i]=="-":
            return False
    for i in range(len(n)):
        if n[i]=="+" or n[i]=="-":
            count+=1
    if count>1:
        return False
     
    count=0
    for i in range(len(n)):
        if n[i]==".":
            count+=1
    if count==1:
        con1=True
    else:
        return False
    if con1==True:
        idx=n.find(".")
        if n[idx+1].isdigit():
            con2=True
        else:
            return False
    if con2==True:
        for i in range(len(n)):
            if n[i]=="+" or n[i]=="-" or n[i]==".":
                continue
            else:
                if ord(n[i])>=48 and ord(n[i])<=57:
                    continue
                else:
                    return False
        else:
            return True
for i in range(t):
    n=str(input())           
    res=val_float(n)
    print(res)
    