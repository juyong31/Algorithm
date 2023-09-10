from collections import deque

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
cnt = 0
for _ in range(m):
  a,b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)
  
def bfs(x):
  global cnt
  queue = deque()
  queue.append(x)
  visited[x] = True
  
  while queue:
    number = queue.popleft()
    
    for i in graph[number]:
      if(visited[i] == False):
        queue.append(i)
        cnt += 1
        visited[i] = True
        
  

bfs(1)
print(cnt)