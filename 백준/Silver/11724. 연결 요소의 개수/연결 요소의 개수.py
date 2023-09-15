import sys
sys.setrecursionlimit(10000)

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
cnt = 0
for _ in range(m):
  a,b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)
  
def dfs(graph, v, visited):
  visited[v] = True
  
  for i in graph[v]:
    if(visited[i] == False):
      dfs(graph, i, visited)

for i in range(1,n+1):
  if(visited[i] == False):
    dfs(graph, i, visited)
    cnt += 1
  
print(cnt)