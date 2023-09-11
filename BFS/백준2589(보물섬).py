# bfs를 돌리는데, queue에서 빠질 때 마다 전 값 + 1 한 값을 해당 위치에 저장해줌

from collections import deque

n, m = map(int, input().split())
graph = []
dx = [1,-1,0,0]
dy = [0,0,1,-1]
for _ in range(n):
  graph.append(list(input()))
totalNum = 0

def bfs(x,y):
  queue = deque()
  queue.append((x,y))
  maxcnt = 0
  visited = [[0]*(m) for _ in range(n)]
  visited[x][y] = 1
  
  
  while queue:
    kx, ky = queue.popleft()
  
    for v in range(4):
      ix = dx[v] + kx
      iy = dy[v] + ky
      if(0<=ix<n and 0<=iy<m and visited[ix][iy] == 0 and graph[ix][iy] == 'L'):
        visited[ix][iy] = visited[kx][ky] + 1
        maxcnt = max(maxcnt, visited[ix][iy])
        queue.append((ix,iy))
  
  return maxcnt-1

for i in range(n):
  for j in range(m):
    if(graph[i][j] == 'L'):
      totalNum = max(totalNum, bfs(i,j))
      
print(totalNum)