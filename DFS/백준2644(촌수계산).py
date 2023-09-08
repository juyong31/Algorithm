import sys
sys.setrecursionlimit(100000)

n = int(input())
num1,num2 = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
result = []

for _ in range(m):
  x,y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)

def dfs(a, cnt):
  if(a == num2):
    result.append(cnt)
  
  visited[a] = True
  cnt += 1

  for i in graph[a]:
    if(visited[i] == False):
      dfs(i, cnt)

dfs(num1, 0)
if(len(result) == 0):
  print(-1)
else:
  print(result[0])
