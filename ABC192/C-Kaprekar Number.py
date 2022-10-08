N, K = input().split()
A = []
c, d= '', ''
for i in N:
    A.append(int(i))
A.sort()
for i in A:
    c += str(i)
print(c)
A.sort(reverse=True)
for i in A:
    d += str(i)
print(c)

