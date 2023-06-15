# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby
for key, group in groupby(input()):
   print('({}, {})'.format(len(list(group)), key), end=" ")
