# graph 에서 1일 경우 cnt = 1로 초기화 후 bfs 수행
# bfs안에서 1을 만날 때 마다 1씩 +
# bfs수행종료 후 cnt를 res[]에다가 저장
# res.sort() 후, len(res)와 res의 각 항목 출력

from collections import deque

n = int(input())
graph = []
for _ in range(n):
  graph.append(list(map(int, input())))
  
res = []
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x, y):
  queue = deque()
  queue.append((x,y))
  global cnt
  graph[x][y] = 0
  
  
  while queue:
    ix, iy = queue.popleft()
    for v in range(4):
      kx = ix+dx[v]
      ky = iy+dy[v]
      if(0<=kx<n and 0<=ky<n and graph[kx][ky] == 1):
        cnt += 1
        queue.append((kx, ky))
        graph[kx][ky] = 0
  
  

for i in range(n):
  for j in range(n):
    if(graph[i][j] == 1):
      cnt = 1
      bfs(i,j)
      res.append(cnt)
      
res.sort()
print(len(res))
for q in res:
  print(q)