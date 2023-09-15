import sys
sys.setrecursionlimit(100000)

n = int(input())
num1, num2 = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
result = []
cnt = 0

for i in range(m):
  parent, child = map(int, input().split())
  graph[parent].append(child)
  graph[child].append(parent)

def dfs(x, cnt):
  if(x == num2):
    result.append(cnt)
  
  cnt += 1
  visited[x] = True
  
  for i in graph[x]:
    if(visited[i] == False):
      dfs(i, cnt)
  
dfs(num1, 0)

if(len(result) == 0):
  print(-1)
else:
  print(result[0])