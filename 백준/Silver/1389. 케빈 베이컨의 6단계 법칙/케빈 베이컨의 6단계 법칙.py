from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)
res = [0]
minNum = 101

def bfs(x,q):
  dp[x] = 0
  queue = deque()
  queue.append(x)
  
  while queue:
    index = queue.popleft()
    for i in graph[index]:
      if(dp[i] == -1):
        dp[i] = dp[index]+1
        queue.append(i)


for k in range(1,n+1):
  cnt = 0
  for q in range(1,n+1):
    dp = [-1 for _ in range(n+1)]
    bfs(k,q)
  cnt = sum(dp)+1
  res.append(cnt)
  minNum = min(minNum, cnt)


print(res.index(minNum))