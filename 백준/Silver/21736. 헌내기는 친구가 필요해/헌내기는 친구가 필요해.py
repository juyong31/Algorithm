from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(list(map(str, input())))
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x,y):
  queue = deque()
  queue.append((x,y))
  graph[x][y] = 'X'
  cnt = 0
  
  while queue:
    ix, iy = queue.popleft()
    for v in range(4):
      vx = ix + dx[v]
      vy = iy + dy[v]
      if(0 <= vx < n and 0 <= vy < m and graph[vx][vy] != 'X'):
        if(graph[vx][vy] == 'P'):
          cnt += 1
        queue.append((vx,vy))
        graph[vx][vy] = 'X'
  
  if(cnt == 0):
    print('TT')
  else:
    print(cnt)
  

for i in range(n):
  for j in range(m):
    if(graph[i][j] == 'I'):
      bfs(i,j)