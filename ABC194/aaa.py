N = int(input())
A = list(map(int, input().split()))
c = 0
for i in range(2, N+1):
    n=i-1
    if 1 == n:
        c += (A[i-1] - A[0])**2
    else:
        for j in range(1, i):
            c += (A[i-1] - A[j-1])**2
print(c)