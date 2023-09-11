from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
for _ in range(m):
  a,b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)
cnt = 0
  
def bfs(x):
  queue = deque()
  queue.append(x)
  visited[x] = True
  
  while queue:
    index = queue.popleft()
    for v in graph[index]:
      if(visited[v] == False):
        visited[v] = True
        bfs(v)



for i in range(1, n+1):
  if(visited[i] == False):
    bfs(i)
    cnt += 1

print(cnt)