# 단 방향으로 그래프 구성
# visited를 모두 False로 때리고
# 삭제할 노드에 대해서만 True로 설정해둠
# root노드부터 dfs 돌리는데, visited = False여야함
# 만약 노드의 자식이 없으면, cnt + 1
import sys
sys.setrecursionlimit(100000)

n = int(input())
graph = [[] for _ in range(n)]
visited = [False for _ in range(n)]
index = list(map(int, input().split()))
for v in range(n):
  if(index[v] == -1):
    root = v
  else:
    graph[index[v]].append(v)
k = int(input())
visited[k] = True

cnt = 0

def dfs(v):
  global cnt
  visited[v] = True

  for i in graph[v]:
    if(visited[i] == False):
      if(len(graph[i]) != 0):
        dfs(i)
      else:
        cnt += 1
    elif(k == i and len(graph[v]) == 1):
      cnt += 1

if(root == k):
  print(0)
elif(n == 2):
  print(1)
else:
  dfs(root)
  print(cnt)