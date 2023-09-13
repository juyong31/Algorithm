# 좌표가 -로 주어질 수 있기때문에 abs를 꼭 해줘야함
from collections import deque
res = []

t = int(input())
for _ in range(t):
  n = int(input())
  startX, startY = map(int, input().split())
  store = []
  for _ in range(n):
    store.append(list(map(int, input().split())))
  endX, endY = map(int, input().split())
  visited = [False for _ in range(n+1)]
  
  def bfs():
    queue = deque()
    queue.append([startX, startY])
    while queue:
      x, y = queue.popleft()
      if(abs(endX-x)+abs(endY-y) <= 1000):
        res.append('happy')
        return
      for i in range(n):
        ix, iy = store[i][0], store[i][1]
        if(abs(ix-x) + abs(iy-y) <= 1000 and visited[i] == False):
          queue.append([ix,iy])
          visited[i] = True
    
    res.append('sad')

  bfs()
for v in res:
  print(v)