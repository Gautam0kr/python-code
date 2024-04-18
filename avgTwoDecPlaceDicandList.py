if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    res=[]
    for name in student_marks:
        if name==query_name:
            res.append(student_marks[name])
    sum=0
    for marks in res[0]:
        sum+=marks
    avg=sum/3
    print(f"{avg:.2f}")