import sys
sys.setrecursionlimit(10000)

t = int(input())
result = []
for _ in range(t):
  m, n, k = map(int, input().split())
  graph = [[0]*m for _ in range(n)]
  cnt = 0
  dx = [0,0,1,-1]
  dy = [1,-1,0,0]
  for _ in range(k):
    x, y = map(int, input().split())
    graph[y][x] = 1
    
  def dfs(graph, x, y):
    graph[x][y] = 0
    
    for v in range(4):
      ix = dx[v] + x
      iy = dy[v] + y
      if(ix >= 0 and ix < n and iy >= 0 and iy < m and graph[ix][iy] == 1):  
        dfs(graph,ix,iy)

    
  for i in range(n):
    for j in range(m):
      if(graph[i][j] == 1):
        dfs(graph,i,j)
        cnt += 1

  result.append(cnt)

for q in result:
  print(q)