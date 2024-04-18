def grade(score):
    if score>75 and score<=100:
        print("Grade: First")
    elif score>60:
        print("Grade: Second")
    elif score>50:
        print("Grade: Third")
    elif score>0:
        print("Fail")
    else:
        print("Invalid score!")
        
score=float(input("Enter your score: "))
grade(score)