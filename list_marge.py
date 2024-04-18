def input_list():
    li=[]
    n=int(input("Enter numbers of elements in list: "))
    print("Enter elements:")
    for i in range(n):
         el=int(input())
         li.append(el)
    return li

print("list1:")
list1=input_list()

print("List2:")
list2=input_list()

merged_list=list1 + list2
merged_list=merged_list.sort()
print("Merged and sorted list :")
print(merged_list)