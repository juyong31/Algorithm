n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
cnt = 0

for _ in range(m):
  a,b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)
  
def dfs(graph, v, visited):
  visited[v] = True
  global cnt
  for i in graph[v]:
    if(visited[i] == False):
      cnt += 1
      dfs(graph, i, visited)
  
dfs(graph,1,visited)

print(cnt)