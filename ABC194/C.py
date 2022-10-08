N = int(input())
A = list(map(int, input().split()))

c = pow(A[1] - A[0], 2)
for i in range(2, N):
    for j in range(0, i):
        c += pow(A[i] - A[j], 2)
print(c)