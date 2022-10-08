N = int(input())
cou = 0
if N <=999:
    a = 0
elif N <= 999999:
    a = 1
    b = N - 1000
    for i in range(0,b+1):
        cou += 1
    print(cou * 1)
elif N <= 999999999:
    a = 2
    b = N - 1000000
    for i in range(0, b+1):
        cou += 1
    print(999000+cou*a)
elif N <= 999999999999:
    a = 3
    b = N - 1000000
    for i in range(0, b+1):
        cou += 1
    print(1998999000+cou*a)
elif N <= 999999999999999:
    a = 4
elif N == 1000000000000000:
    a = 5