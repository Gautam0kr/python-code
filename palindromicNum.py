for i in range(1, int(input()) + 1): 
    l=[*range(1, i), *range(i, 0, -1)]
    print(*[int(x) for x in l], sep="")
