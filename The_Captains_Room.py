# Enter your code here. Read input from STDIN. Print output to STDOUT
k,arr = int(input()),list(map(int, input().split()))

myset = set(arr)

print(((sum(myset)*k)-(sum(arr)))//(k-1))
