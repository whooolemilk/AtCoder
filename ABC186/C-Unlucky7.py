#Unlucky7
N = int(input())
n = []
ans = []
for i in range(1, N+1):
    if "7" not in str(i):
        n.append(i)
for i in n:
    if "7" not in str(oct(i)[2:]):
        ans.append(oct(i))
print(len(ans))
