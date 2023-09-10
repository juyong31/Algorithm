# 1~n까지 각 항목별로 나머지 숫자에게 도달하는 리스트(dp)작성
# res 에다가 각 항목별로 나머지 숫자들에게 도달하기위한 값(sum) 저장
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
  cnt = sum(dp)+1 #자기자신은 -1로 저장되어 있기 때문에, 자기자신을 제외하기 위해 +1
  res.append(cnt)
  minNum = min(minNum, cnt)


print(res.index(minNum))