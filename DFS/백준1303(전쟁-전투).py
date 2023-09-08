import sys
sys.setrecursionlimit(100000)

m, n = map(int, input().split())
total_w = 0
total_b = 0
graph = []
dx = [0,0,1,-1]
dy = [1,-1,0,0]
for _ in range(n):
  graph.append(list(input()))

def dfs_w(graph, x, y):
  global white
  graph[x][y] = 'X'

  for v in range(4):
    ix = dx[v] + x
    iy = dy[v] + y
    if(0 <= ix < n and 0 <= iy < m and graph[ix][iy] == 'W'):
      white += 1
      dfs_w(graph, ix, iy)

def dfs_b(graph, x, y):
  global blue
  graph[x][y] = 'X'
  
  for v in range(4):
    ix = dx[v] + x
    iy = dy[v] + y
    if(0 <= ix < n and 0 <= iy < m and graph[ix][iy] == 'B'):
      blue += 1
      dfs_b(graph, ix, iy)


for i in range(n):
  for j in range(m):
    if(graph[i][j] == 'W'):
      white = 1
      dfs_w(graph, i, j)
      total_w += white*white
    elif(graph[i][j] == 'B'):
      blue = 1
      dfs_b(graph,i,j)
      total_b += blue*blue
      
print(total_w, total_b)