import sys
sys.setrecursionlimit(100000)

res = []
dx = [1,1,0,-1,-1,-1,0,1]
dy = [0,-1,-1,-1,0,1,1,1]
while True:
  w, h = map(int, input().split())
  if(w == 0 and h == 0):
    break
  cnt = 0
  graph = []
  for _ in range(h):
    graph.append(list(map(int, input().split())))

  def dfs(graph, x, y):
    graph[x][y] = 0
    for v in range(8):
      ix = x + dx[v]
      iy = y + dy[v]

      if(ix >= 0 and ix < h and iy >= 0 and iy < w and graph[ix][iy] == 1):
        dfs(graph,ix,iy)
  
  
  for i in range(h):
    for j in range(w):
      if(graph[i][j] == 1):
        cnt += 1
        dfs(graph, i, j)
  res.append(cnt)

for k in res:
  print(k)
