from collections import deque
import copy
n, m = map(int, input().split())
graph = []
res = 0
queue = deque()
dx = [0,0,1,-1]
dy = [1,-1,0,0]

for _ in range(n):
  graph.append(list(map(int, input().split())))
  
for i in range(n):
    for j in range(m):
      if(graph[i][j] == 2):
        queue.append((i,j))
          
def bfs():
  global res
  index_graph = copy.deepcopy(graph)
  index_queue = copy.deepcopy(queue)
  
  while index_queue:
    x,y = index_queue.popleft()
    for k in range(4):
      index_x = dx[k] + x
      index_y = dy[k] + y
      if(0 <= index_x < n and 0 <= index_y < m and index_graph[index_x][index_y] == 0):
        index_queue.append((index_x, index_y))
        index_graph[index_x][index_y] = 2
        
  total = 0
  for v in range(n):
    for q in range(m):
      if(index_graph[v][q] == 0):
        total += 1
  res = max(res, total)
  
def makeWall(cnt):
  if(cnt == 3):
    bfs()
    return
    
  for k in range(n):
    for l in range(m):
      if(graph[k][l] == 0):
        graph[k][l] = 1
        makeWall(cnt+1)
        graph[k][l] = 0
          
makeWall(0)
print(res)