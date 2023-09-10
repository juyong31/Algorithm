# 토마토가 익어있는 위치(1인 위치) 찾아서 queue에 넣기
# bfs를 수행
# for 문으로 전체를 탐색하는데, 만약 익지않은 토마토가 있을경우(0이 있을경우) -1출력 후 종료
# 없을 경우 max값 출력
from collections import deque

m, n = map(int, input().split())
graph = []
res = 0
for _ in range(n):
  graph.append(list(map(int, input().split())))
dx = [0,0,1,-1]
dy = [1,-1,0,0]

queue = deque()
for i in range(n):
  for j in range(m):
    if(graph[i][j] == 1):
      queue.append((i,j))

def bfs():
  while queue:
    x,y = queue.popleft()
    for v in range(4):
      ix = x + dx[v]
      iy = y + dy[v]
      if(0<=ix<n and 0<=iy<m and graph[ix][iy] == 0):
        graph[ix][iy] = graph[x][y] + 1
        queue.append((ix,iy))
  

bfs()
for i in range(n):
  for j in range(m):
    if(graph[i][j] == 0):
      print(-1)
      exit(0)
    else:
      res = max(res, graph[i][j])
      
print(res-1)