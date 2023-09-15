import sys
sys.setrecursionlimit(100000)

n, m, k = map(int, input().split())
graph = [[0]*(m) for _ in range(n)]
res = []
dx = [0,0,1,-1]
dy = [1,-1,0,0]

for _ in range(k):
  y1,x1,y2,x2 = map(int, input().split())
  for i in range(x1, x2):
    for j in range(y1, y2):
      graph[i][j] = 1

def dfs(graph, x, y):
  global cnt
  graph[x][y] = 1
  cnt += 1

  for v in range(4):
    ix = dx[v]+x
    iy = dy[v]+y
    if(0 <= ix < n and 0 <= iy < m and graph[ix][iy] == 0):
      dfs(graph,ix,iy)

for i in range(n):
  for j in range(m):
    if(graph[i][j] == 0):
      cnt = 0
      dfs(graph, i, j)
      res.append(cnt)

res.sort()
print(len(res))
for q in res:
  print(q, end = ' ')