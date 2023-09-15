from collections import deque

n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
  a,b = map(int, input().split())
  graph[b].append(a)

def bfs(x):
  queue = deque()
  queue.append(x)
  visited[x] = 0
  index = 1

  while queue:
    ix = queue.popleft()
    for v in graph[ix]:
      if(visited[v] == -1):
        queue.append(v)
        visited[v] = visited[ix] + 1
        index += 1
  return index
        
maxNum = 0
res = []
for i in range(1, n+1):
  if(len(graph[i]) != 0):
    visited = [-1 for _ in range(n+1)]
    cnt = bfs(i)
    if(maxNum < cnt):
      res = []
      res.append(i)
      maxNum = cnt
    elif(maxNum == cnt):
      res.append(i)

res.sort()
print(*res)