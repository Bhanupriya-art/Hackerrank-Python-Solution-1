# Enter your code here. Read input from STDIN. Print output to STDOUT
def isstrictsuperset(a,b):
    # true if a is a strict superset of b
    return b.issubset(a) and not(a.issubset(b))

a = set(int(x) for x in input().split(' '))
n = int(input())
res = True

for _ in range(n):
    b = set(int(x) for x in input().split(' '))
    res &= isstrictsuperset(a,b)
    
print(res)
