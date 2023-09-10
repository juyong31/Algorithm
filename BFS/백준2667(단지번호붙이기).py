from collections import deque

n = int(input())
graph = []
res = []
dx = [0,0,1,-1]
dy = [1,-1,0,0]
for _ in range(n):
  graph.append(list(map(int, input())))
  
def bfs(x,y):
  global cnt
  queue = deque()
  queue.append((x,y))
  graph[x][y] = 0
  
  while queue:
    ix, iy = queue.popleft()
    
    for v in range(4):
      vx = dx[v] + ix
      vy = dy[v] + iy
      if(0<=vx<n and 0<=vy<n and graph[vx][vy] == 1):
        graph[vx][vy] = 0
        cnt += 1
        queue.append((vx,vy))
  

for i in range(n):
  for j in range(n):
    if(graph[i][j] == 1):
      cnt = 1
      bfs(i,j)
      res.append(cnt)

res.sort()
print(len(res))
for k in res:
  print(k)