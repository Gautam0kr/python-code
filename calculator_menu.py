def calculator(operator, num1, num2):
    if operator=="1":
        print("sum of",num1, " and ",num2, " is: ", num1+num2)
    elif operator=="2":
        print("Differnce of",num1, " and ",num2, " is: ", num1-num2)
    elif operator=="3":
        print("Product of",num1, " and ",num2, " is: ", num1*num2)
    elif operator=="4":
        print("division of",num1, " and ",num2, " is: ", num1/num2)
    else:
        print("Invalid operator!")

num1=float(input("Enter first num: "))       
print("Choose operator:")
print("1. +", "\n2. -", "\n3. *", "\n4. /")
operator=str(input("Enter(1, 2, 3, 4): "))
num2=float(input("Enter second num: "))
calculator(operator, num1, num2) 