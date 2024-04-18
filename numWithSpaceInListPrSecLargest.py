if __name__ == '__main__':
    n = int(input())
    arr =list(map(int, input().split()))
    arr.sort()
    print(arr)
    for i in range(-2, -(n+1), -1):
        if arr[-1]>arr[i]:
            print(arr[i])
            break