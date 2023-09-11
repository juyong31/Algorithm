# 움직일 수 있는 곳 마다 (기존위치 + 1) 해주고
# 이동하려는 칸과 현 위치가 같으면 그 위치 값을 return

from collections import deque

res = []

t = int(input())
for _ in range(t):
  n = int(input())
  startX, startY = map(int, input().split())
  endX, endY = map(int, input().split())
  graph = [[0]*n for _ in range(n)]
  dx = [2,1,-1,-2,-2,-1,1,2]
  dy = [1,2,2,1,-1,-2,-2,-1]

  def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    
    while queue:
      kx, ky = queue.popleft()
      if(kx == endX and ky == endY):
        res.append(graph[kx][ky])
        break
      
      for v in range(8):
        ix = dx[v] + kx
        iy = dy[v] + ky
        if(0<=ix<n and 0<=iy<n and graph[ix][iy] == 0):
          graph[ix][iy] = graph[kx][ky] + 1
          queue.append((ix,iy))


  bfs(startX,startY)
  
for q in res:
  print(q)