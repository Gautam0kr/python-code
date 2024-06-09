import math
ab=float(input())
bc=float(input())

x=bc/ab

a=math.degrees(math.atan(x))

res=90-a
print(str(round(res))+'\xb0')


# #same thing
# import math
# ab=int(input())
# bc=int(input())
# print(str(round(math.degrees(math.atan(ab/bc))))+'\xb0')