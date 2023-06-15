
import string
# Complete the solve function below.
def solve(s):
    l=s.split(" ")
    s=''
    for i in l:
        s=s+i.capitalize()+' '
        
    return s

