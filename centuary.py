def centuary(score):
    if score>=100:
        print("Centuary")
    elif score>=50:
        print("Half centuary")
    elif score>0:
        print("No centuary")
    else:
        print("Invalid score!")
        
score=float(input("Enter your score: "))
centuary(score)