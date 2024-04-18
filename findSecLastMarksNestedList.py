if __name__ == '__main__':
    record=[]
    for _ in range(int(input())):
        rec=[]
        name = input()
        rec.append(name)
        score = float(input())
        rec.append(score)
        record.append(rec)
        
    record.sort()
    score=[]
    for i in range(len(record)):
        for j in range(1):
            score.append(record[i][1])
            
    score.sort()
    min=score[0]
    for i in range(len(score)):
        if score[i]>min:
            min=score[i]
            break
    for i in range(len(record)):
        for j in range(1):
            if record[i][1]==min:
                print(record[i][0])
            
            