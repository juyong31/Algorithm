import sys
sys.setrecursionlimit(10000)

n = int(input())
graph = []
visited = [[False]*n for _ in range(n)]
cnt = 0
result = []
dx = [1,-1,0,0]
dy = [0,0,-1,1]
for _ in range(n):
  graph.append(list(map(str, input())))
  
def dfs(graph, x, y, visited):
  visited[x][y] = True
  color = graph[x][y]
  
  for i in range(4):
    ix = dx[i] + x
    iy = dy[i] + y
    if(ix >= 0 and ix < n and iy >= 0 and iy < n and visited[ix][iy] == False):
      if(graph[ix][iy] == color):
        dfs(graph, ix, iy, visited)
  

for i in range(n):
  for j in range(n):
    if(visited[i][j] == False):
      dfs(graph, i, j, visited)
      cnt += 1
    
result.append(cnt)
cnt = 0
visited = [[False]*n for _ in range(n)]

for i in range(n):
  for j in range(n):
    if(graph[i][j] == 'G'):
      graph[i][j] = 'R'

for i in range(n):
  for j in range(n):
    if(visited[i][j] == False):
      dfs(graph, i, j, visited)
      cnt += 1

result.append(cnt)

for i in result:
  print(i, end = ' ')