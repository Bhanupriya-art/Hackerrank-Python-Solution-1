# Enter your code here. Read input from STDIN. Print output to STDOUT
_, a = input(), set(input().split())
_, b = input(), set(input().split())
print(len(a.symmetric_difference(b)))
