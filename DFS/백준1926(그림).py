import sys
sys.setrecursionlimit(1000000)

n, m = map(int, input().split())

graph = []
for _ in range(n):
  graph.append(list(map(int, input().split())))
cnt = 0
area = 0
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(graph, x, y):
  global index
  graph[x][y] = 0
  
  for v in range(4):
    ix = dx[v] + x
    iy = dy[v] + y
    if(ix >= 0 and ix < n and iy >= 0 and iy < m and graph[ix][iy] == 1):
      index += 1
      dfs(graph, ix, iy)



for i in range(n):
  for j in range(m):
    if(graph[i][j] == 1):
      index = 1
      dfs(graph, i, j)
      cnt += 1
      if(index > area):
        area = index
        
print(cnt)
print(area)