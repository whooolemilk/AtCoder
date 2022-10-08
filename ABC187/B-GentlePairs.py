N = int(input())
x = []
cou = 0
for i in range(N):
    x.append(list(map(int,input().split())))

for i in range(N):
    for j in range(i+1, N):
        Y = x[i][1] - x[j][1]
        X = x[i][0] - x[j][0]
        a = Y / X
        if -1 <= a <= 1:
            cou += 1

print(cou)