# Enter your code here. Read input from STDIN. Print output to STDOUT
a,b = [set(input().split()) for _ in range(4)][1::2]
print('\n'.join(sorted(a^b, key=int)))
