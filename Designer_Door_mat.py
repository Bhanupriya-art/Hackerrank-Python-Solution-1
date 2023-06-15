# Enter your code here. Read input from STDIN. Print output to STDOUT
R,C = map(int,input().split(' '))
for i in range(1,R,2):
    print((".|."*i).center(C,'-'))
    
print("WELCOME".center(C,'-'))

for i in range(R-2,-1,-2):
    print((".|."*i).center(C,'-'))
