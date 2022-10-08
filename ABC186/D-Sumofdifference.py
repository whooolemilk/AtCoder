#Sum of difference -> TLE
import itertools
N = int(input())
ans = 0
A = list(map(int, input().split()))
# for c in itertools.combinations(A, 2):
#     ans += abs(c[0]-c[1])
# print(ans)

s = 0
A.sort()
for i in range(N):
    ans += A[i] * i - s
    s += A[i]
print(A)
