Days={1:"sunday", 2:"monday",3:"tuesday",4:"wednesday",5:"thursday",6:"friday",7:"saturday"}
'''for i in range(1, len(Days)+1):
    if (Days[i][0]=="s"):
        del Days[i]
print(Days)'''
tempdic={}
j=1
for i in range(1, len(Days)+1):
        if i>=2:
            tempdic[j]=Days[i]
            j+=1
tempdic[j]=Days[1]
print(tempdic)

tempdic2={}
j=1
for i in range(1, len(Days)+1):
    if i>=4:
        tempdic2[j]=Days[i]
        j+=1
for i in range(1, len(Days)):
    if i<=3:
        tempdic2[j]=Days[i]
        j+=1
print(tempdic2)
    
    
    