X = int(input())
for i in range(10000):
    if 100 * i > X:
        break
print(100 * i - X)