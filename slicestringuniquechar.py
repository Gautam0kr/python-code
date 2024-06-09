def merge_the_tools(string, k):
    i=0
    t=k
    r=len(string)//k
    for _ in range(r):
        templist=list(string[i:t])
        l=[]
        for c in templist:
            if c in l:
                continue    
            else:
                l.append(c)       
        i=t
        t+=k
            
        print(("").join(l))
        
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)




# #using textwrap and dict
# import textwrap
# def merge_the_tools(string, k):
#     temp=textwrap.wrap(string, k)
#     for c in temp:
#         print("".join(dict.fromkeys(c)))
    
# if __name__ == '__main__':
#     string, k = input(), int(input())
#     merge_the_tools(string, k)