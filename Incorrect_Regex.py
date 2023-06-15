# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
T = int(input())
for _ in range(T):
    try:
        re.compile(input())
        print(True)
    except Exception:
        print(False)
