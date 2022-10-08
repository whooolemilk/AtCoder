#Blocks on Grid
import numpy as np
H, W = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(H)]
grid = np.array(grid)
print(np.sum(grid - np.min(grid)))