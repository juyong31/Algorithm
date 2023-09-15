import sys, copy
sys.setrecursionlimit(100000)

n = int(input())
graph = []
res = 0
maxNum = 0
dx = [1,-1,0,0]
dy = [0,0,1,-1]

for i in range(n):
  graph.append(list(map(int, input().split())))
  
  for j in range(n):
    maxNum = max(maxNum, graph[i][j])
    
def dfs(IndexGraph, x, y, depth):
  IndexGraph[x][y] = depth
  
  for v in range(4):
    ix = dx[v] + x
    iy = dy[v] + y
    if(0 <= ix < n and 0 <= iy < n and IndexGraph[ix][iy] > depth):
      dfs(IndexGraph, ix, iy, depth)


for t in range(maxNum):
  IndexGraph = copy.deepcopy(graph)
  cnt = 0
  for i in range(n):
    for j in range(n):
      if(IndexGraph[i][j] > t):
        cnt += 1
        dfs(IndexGraph, i, j, t)
  res = max(res, cnt)

print(res)