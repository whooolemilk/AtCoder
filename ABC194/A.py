A, B = map(int,input().split())
if 15 <= A+B and 8 <= B:
    print('1')
elif 10 <= A+B and 3 <= B:
    print('2')
elif 3 <= A+B:
    print('3')
else:
    print('4')