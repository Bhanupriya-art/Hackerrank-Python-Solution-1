if __name__ == '__main__':
    disc={}
    s=list()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score in disc:
            disc[score].append(name)
        else:
            disc[score]=[name]
        if score not in s:
            s.append(score)    
            
    m=min(s)
    s.remove(m)
    m1=min(s)
    disc[m1].sort()
    for i in disc[m1]:
        print(i)
