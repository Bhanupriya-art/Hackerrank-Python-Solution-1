# Enter your code here. Read input from STDIN. Print output to STDOUT
a = set()
[a.add(input()) for _ in range(int(input()))]
print(len(a))
