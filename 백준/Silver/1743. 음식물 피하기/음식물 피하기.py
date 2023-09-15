import sys
sys.setrecursionlimit(10000)

n, m, k = map(int, input().split())

graph = [[0]*m for _ in range(n)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
maxNum = 0
for _ in range(k):
  a,b = map(int, input().split())
  graph[a-1][b-1] = 1

def dfs(graph, x, y):
  graph[x][y] = 0
  global cnt
  
  for v in range(4):
    ix = dx[v]+x
    iy = dy[v]+y
    if(0 <= ix < n and 0 <= iy < m and graph[ix][iy] == 1):
      cnt += 1
      dfs(graph,ix,iy)


for i in range(n):
  for j in range(m):
    if(graph[i][j] == 1):
      cnt = 1
      dfs(graph, i, j)
      maxNum = max(maxNum, cnt)
      
print(maxNum)