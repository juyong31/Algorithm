import sys
sys.setrecursionlimit(100000)

n = int(input())
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
res = [0 for _ in range(n+1)]
for _ in range(n-1):
  a,b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)
  
def dfs(graph, v, visited):
  visited[v] = True
  
  for k in graph[v]:
    if(visited[k] == False):
      res[k] = v
      dfs(graph, k, visited)


dfs(graph, 1, visited)

for q in range(2, n+1):
  print(res[q])