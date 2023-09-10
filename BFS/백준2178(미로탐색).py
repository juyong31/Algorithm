from collections import deque

n, m = map(int, input().split())

graph = []
for _ in range(n):
  graph.append(list(map(int, input())))
dx = [0,0,1,-1]
dy = [1,-1,0,0]


def bfs(x,y):
  queue = deque()
  queue.append((x,y))
  
  while queue:
    x, y = queue.popleft()
    
    for v in range(4):
      ix = dx[v]+x
      iy = dy[v]+y
      
      if(0 <= ix < n and 0 <= iy < m and graph[ix][iy] == 1):
        graph[ix][iy] = graph[x][y] + 1
        queue.append((ix,iy))



bfs(0,0)
print(graph[n-1][m-1])