if __name__ == '__main__':
    N = int(input())
    list=[]
    for i in range(N):
        fun=input().split()
        
        if fun[0]=="insert":
            list.insert(int(fun[1]), int(fun[2]))
    
        elif fun[0]=="print":
            print(list)
        elif fun[0]=="remove":
            list.remove(int(fun[1]))
        elif fun[0]=="append":
            list.append(int(fun[1]))
        elif fun[0]=="sort":
            list.sort()
        elif fun[0]=="pop":
            list.pop()
        elif fun[0]=="reverse":
            list.reverse()
        else:
            continue  
        
