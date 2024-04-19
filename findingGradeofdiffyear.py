def input_marks():
    sum=0
    for _ in range(5):
        m=int(input("Enter marks: "))
        sum+=m
    p=sum/5
    return p

def Grade(p):
    if p>60 and p<=100:
        print("Grade: First")
    elif p>50:
        print("Grade: Second")
    elif p>0:
        print("Grade: Third")
    else:
        print("Invalid Marks!")

def year(n):
    stu=int(input(f"Enter num of stu in {n} year: "))
    for _ in range(stu):
        p=input_marks()
        Grade(p)

n=int(input("Enter year for which you want to check grade: "))
year(n)