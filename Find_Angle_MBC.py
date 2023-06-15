# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import degrees, atan2

AB = float(input())
BC = float(input())

MBC = round(degrees(atan2(AB, BC)))
print((str(MBC)), chr(176), sep='')
