#ascending to descending
li=[]
print("Enter five numbers: ")
for i in range(5):
    el=int(input())
    li.append(el)
    
li.sort(reverse=True)
print("Numbers in descending order: ")
for num in li:
    print(num)