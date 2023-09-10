from collections import deque
t = int(input())
res = []
for _ in range(t):
  m, n, k = map(int, input().split())
  graph = [[0]*(m) for _ in range(n)]
  dx = [0,0,1,-1]
  dy = [1,-1,0,0]
  cnt = 0
  for _ in range(k):
    a,b = map(int ,input().split())
    graph[b][a] = 1

  def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 0
    
    while queue:
      ix,iy = queue.popleft()
      for v in range(4):
        vx = ix+dx[v]
        vy = iy+dy[v]
        if(0<=vx<n and 0<=vy<m and graph[vx][vy] == 1):
          graph[vx][vy] = 0
          queue.append((vx,vy))


  for i in range(n):
    for j in range(m):
      if(graph[i][j] == 1):
        cnt += 1
        bfs(i,j)
  res.append(cnt)

for k in res:
  print(k)