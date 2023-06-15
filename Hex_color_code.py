# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
in_css = False
n = int(input())
for _ in range(n):
    line=input()
    if '{' in line:
        in_css = True
    elif '}' in line:
        in_css = False
    elif in_css:
        for color in re.findall('#[0-9a-fA-F]{3,6}',line):
            print(color)
