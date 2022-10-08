N = int(input())
sa = 0
ab = []
for i in range(N):
    A, B = map(int,input().split())
    sa -= A
    ab.append(A + B + A)
ab.sort()
ans = 0
while sa <= 0:
    sa +=ab.pop()
    ans += 1
print(ans)
        