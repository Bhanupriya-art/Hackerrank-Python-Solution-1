import numpy

n,m=map(int,input().split())

lista=[list(map(int,input().split())) for i in range(n)]

ar=numpy.array(lista)

print(max(numpy.min(ar,axis=1)))
