#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    p=sorted(arr,key=lambda row:row[k])
    for i in range(len(p)):
        for j in range(len(p[i])):
            print(p[i][j],end=' ')
        print()
