# 整数 1 つ
N = int(input())

# 整数複数個
N, K = map(int, input().split())

# 整数 N 個 (改行区切り)
L = [int(input()) for i in range(N)]

# 整数 N 個 (スペース区切り)
A = list(map(int, input().split()))

# 整数 (縦 H 横 W の行列)
S = [list(map(int, input().split())) for i in range(H)]

#整数２つを行ごとに
ab = [map(int, input().split()) for _ in range(n)]
a, b = [list(i) for i in zip(*ab)]