from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))
  graph[b].append((a, c))


def bfs(start, end):
  visited = [False for _ in range(n+1)]
  queue = deque()
  queue.append((start, 0))
  visited[start] = True
  
  while queue:
    current, length = queue.popleft()
    if(current == end):
      print(length)
      return
    for next, l in graph[current]:
      if(visited[next] == False):
        queue.append((next, l+length))
        visited[next] = True



for _ in range(m):
  n1, n2 = map(int, input().split())
  bfs(n1, n2)