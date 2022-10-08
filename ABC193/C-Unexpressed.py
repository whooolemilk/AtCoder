N = int(input())
out = set()
 
for a in range(2,10**5+1):
    b = 2
    while a**b <= N:
        out.add(a**b)
        b += 1
print(out)
print(N-len(out))