n = int(input())
graph = []
total = 0
index = 1
index_arr = []
dx = [0,0,1,-1]
dy = [1,-1,0,0]

for _ in range(n):
  graph.append(list(map(int, input())))

def dfs(graph, x, y):
  global index
  graph[x][y] = 0
  
  for v in range(4):
    ix = dx[v] + x
    iy = dy[v] + y
    if(ix >= 0 and ix < n and iy >= 0 and iy < n and graph[ix][iy] == 1):
      dfs(graph, ix, iy)
      index += 1
  

for i in range(n):
  for j in range(n):
    if(graph[i][j] == 1):
      dfs(graph, i, j)
      total += 1
      index_arr.append(index)
      index = 1

index_arr.sort()
print(total)
for k in index_arr:
  print(k)