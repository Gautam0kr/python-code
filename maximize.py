#code fails in various test cases
# k, m=map(int, input().split())
# maxnum=[]
# for _ in range(k):
#     temp=list(map(int, input().split()))
    
#     temp.pop(0)
#     temp.sort()
#     maxnum.append(temp[-1])
# res=0
# for num in maxnum:
#     res+=(num ** 2)
# print(res % m)



import itertools

def maximize_value(k, m, lists):
    max_value = 0

    # Generate all possible combinations of elements from the lists
    for combination in itertools.product(*lists):
        # Calculate the value of the expression
        value = sum(x ** 2 for x in combination) % m
        max_value = max(max_value, value)

    return max_value

# Read input
k, m = map(int, input().split())
lists = [list(map(int, input().split()))[1:] for _ in range(k)]

# Calculate and print the maximum value
print(maximize_value(k, m, lists))


