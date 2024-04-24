def Input_marks(sub):
    sum=0
    print(f"Enter marks of all {sub} subjects")
    for i in range(1,sub+1):
        m=(int(input(f"Enter marks of sub{i}: ")))
        sum+=m
    per=sum/sub
    print("your percentage is: ", per)
    if per<=100 and per>60:
        print("And your grade is: FIRST")
    elif per>50:
        print("And your grade is: SECOND")
    elif per>=0:
        print("And your grade is: THIRD")
    else:
        print("Invalid marks!!")
        
def Input_course():
    global sub,stu
    stu=int(input("Enter num of students: "))
    sub=int(input("Enter num of subjects: "))
    print()
for _ in range(5):
    course=input("Enter your course: ")
    for i in range(1, 4):
        print(f"Enter details of year{i}")
        Input_course()
        for j in range(stu):
            Input_marks(sub)
            print()
            if j<stu-1:
                print("Enter marks of Next student: ")
    