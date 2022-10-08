N = int(input())
S = set(input() for i in range(N))
for i in S:
    if "!" + i in S:
        print(i)
        exit()
print('satisfiable')