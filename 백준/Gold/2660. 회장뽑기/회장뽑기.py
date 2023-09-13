# 서로 관계를 저장
# 모든 사람에 대해 돌리기위해 1~n까지 for문수행
# 각 사람별로 다른사람들에게 접근하기 위한 숫자를 저장, 여기서 max값과 current min 값을 min(maxNum, currentMin)
# 최종적으로 currentMin 출력
from collections import deque

n = int(input())
graph = [[] for _ in range(n+1)]
while True:
  a, b = map(int, input().split())
  if(a == -1 and b == -1):
    break
  graph[a].append(b)
  graph[b].append(a)
res = 100

def bfs(x):
  queue = deque()
  queue.append(x)
  visited[x] = 0
  while queue:
    ix = queue.popleft()
    for i in graph[ix]:
      if(visited[i] == -1):
        visited[i] = visited[ix] + 1
        queue.append(i)



result_list = []
for i in range(1, n+1):
  visited = [-1 for _ in range(n+1)]
  bfs(i)
  maxIndex = max(visited)
  if(res > maxIndex):
    result_list = []
    result_list.append(i)
    res = maxIndex
  elif(res == maxIndex):
    result_list.append(i)
print(res, len(result_list))
for v in result_list:
  print(v, end = ' ')