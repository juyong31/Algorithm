import sys
sys.setrecursionlimit(100000)

n = int(input())
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
for _ in range(n-1):
  a,b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)
  
def dfs(v):
  for i in graph[v]:
    if(visited[i] == False):
      visited[i] = v
      dfs(i)


dfs(1)

for q in range(2, n+1):
  print(visited[q])