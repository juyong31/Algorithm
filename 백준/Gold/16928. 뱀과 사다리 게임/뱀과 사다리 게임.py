# ladder와 snake 값을 dict로 저장
# queue에 시작점인 1을 넣고 while queue동안 수행
# 100이면 스톱
# 이동은 주사위 수 만큼 이동할 수 있기 때문에, 현위치(queue.left())에서 for(1,7)을 수행
# 만약 방문한 기록이 없고(visited==False), 100을 넘어가는 것이 아니면 스톱

from collections import deque

n,m = map(int, input().split())
graph = [0 for _ in range(101)]
visited = [False for _ in range(101)]

ladder = dict()
snake = dict()
for _ in range(n):
  x,y = map(int, input().split())
  ladder[x] = y
for _ in range(m):
  x,y = map(int, input().split())
  snake[x] = y

def bfs():
  queue = deque()
  queue.append(1)
  visited[1] = True
  while queue:
    loc = queue.popleft()
    if(loc == 100):
      print(graph[100])
      break
    for i in range(1,7):
      next_loc = loc+i
      if(next_loc in ladder):
        next_loc = ladder[next_loc]
      elif(next_loc in snake):
        next_loc = snake[next_loc]
      if(next_loc <= 100 and visited[next_loc] == False):
        graph[next_loc] = graph[loc]+1
        queue.append(next_loc)
        visited[next_loc] = True


bfs()