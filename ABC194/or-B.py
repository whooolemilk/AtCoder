import sys
import itertools
import math

def comb(n,r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))



N = int(input())
A = list(map(int, input().split()))


c = comb(len(A),2)
print(c)
s = sum(A)
res = 0

for i,v in enumerate(A):
    s -= v
    res += (pow(v,2))*(len(A)-1)-2*v*s


print(res)