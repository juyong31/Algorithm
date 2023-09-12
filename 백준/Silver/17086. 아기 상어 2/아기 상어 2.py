# 1을 다 찾아서 queue에 넣고
# graph안에서 0이 없을 때 까지 돌림(queue에 넣어가면서)
# max값 출력

from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int, input().split())))
dx = [1,1,0,-1,-1,-1,0,1]
dy = [0,1,1,1,0,-1,-1,-1]
maxNum = 0
queue = deque()
for i in range(n):
  for j in range(m):
    if(graph[i][j] == 1):
      queue.append((i,j))
      

def bfs():
  global maxNum
  while queue:
    x,y = queue.popleft()
    for v in range(8):
      ix = x + dx[v]
      iy = y + dy[v]
      if(0<=ix<n and 0<=iy<m and graph[ix][iy] == 0):
        queue.append((ix,iy))
        graph[ix][iy] = graph[x][y] + 1
        maxNum = max(maxNum, graph[ix][iy])
  
bfs()
print(maxNum - 1)