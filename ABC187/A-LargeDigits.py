#Large Digits
A, B = input().split()
sa = 0
sb = 0
for i in A:
    sa += int(i)
for i in B:
    sb += int(i)
if sa >sb:
    print(sa)
else:
    print(sb)