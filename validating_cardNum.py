N=int(input())
def temp(card_num):
    con1=False
    con2=False
    con3=False
    
    if card_num[0]=="4" or card_num[0]=="5" or card_num[0]=="6":
        con1=True
    else:
        print("Invalid")
        return
    if con1==True:
        if len(card_num)==16:
            con2=True
        elif len(card_num)==19:
            pass
        else:
            print("Invalid")
            return
    if con2==True:
        for i in range(16):
            if int(card_num[i])>=0 and int(card_num[i])<=9:
                con3=True
            else:
                print("Invalid")
                return
    if con3==True:
        for i in range(12):
            count=0
            for j in range(1, 4):
                if card_num[i]==card_num[i+j]:
                    count+=1
            
                    if count>=3:
                        print("Invalid")
                        return
        else:
            print("Valid")
            return
                    
        
    con4=False
    con5=False
   
        
    if len(card_num)==19 and con1==True:
        if card_num[4]=="-" and card_num[9]=="-" and card_num[14]=="-":
            con4=True
        else:
            print("Invalid")
            return
    if con4==True:
        for i in range(19):
            if i==4 or i==9 or i==14:
                continue
            else:
                if int(card_num[i])>=0 and int(card_num[i])<=9:
                    con5=True
    else:
        print("Invalid")
        return
    if con5==True:
        for i in range(15):
            if i==4 or i==9 or i==14:
                continue
            else:
                count=0
                for j in range(1, 5):
                    j=i+j
                    
                    if j==4 or j==9 or j==14:
                        continue
                    else:
                        if card_num[i]==card_num[j]:
                            count+=1
                if count>=3:
                    print("Invalid")
                    return       
        else:    
            print("Valid")
            return
for n in range(N):
    card_num=input()               
    temp(card_num)
        
