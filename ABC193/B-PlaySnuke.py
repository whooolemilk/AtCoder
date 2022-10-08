N = int(input())
apx = []
for i in range(N):
    apx.append(list(map(int, input().split())))
ans = []
for i in range(N):
    c = apx[i][2] - apx[i][0]
    if c > 0:
        ans.append(apx[i][1])

if ans == []:
    print("-1")
else:
    print(min(ans))