N = int(input())
A = []
B = []
ans = []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

a = min(A)
ai = A.index(a)

b = min(B)
bi = B.index(b)

if ai == bi:
    ans.append(a + b)

del B[bi]
c = min(B)
ans.append(max(a,c))

print(min(ans))