if __name__ == '__main__':
    n = int(input())
    integer_list =input().split()
    tup=()
    for i in range(n):
        tup+=(int(integer_list[i]), )
        
    print(hash(tup))