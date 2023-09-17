# 0이 아닌 곳 좌표를 찾아서 virus list에 넣는데,
# 넣을 때 number, x좌표, y좌표를 넣어
# virus 를 sort   (sort하면 맨 앞 숫자를 기준으로 정렬)
# queue에 virus를 넣어
# cnt = 0으로 초기화 한 후, queue를 한 번 시행할 때 마다 +1 (queue에 있는 항목들은 모두 수행해야함)
# cnt == 2 이면 break, print(graph[x][y])

from collections import deque

n, k = map(int, input().split())
graph = []
virus = []
dx = [0,0,1,-1]
dy = [1,-1,0,0]
for i in range(n):
  graph.append(list(map(int, input().split())))
  for j in range(n):
    if(graph[i][j] != 0):
      virus.append(((graph[i][j], i, j)))
S,X,Y = map(int, input().split())

def bfs(s,X,Y):
  queue = deque(virus)
  cnt = 0
  while queue:
    if(cnt == s):
      break
    for _ in range(len(queue)):
      number, x, y = queue.popleft()
      for v in range(4):
        ix = dx[v] + x
        iy = dy[v] + y
        if(0<=ix<n and 0<=iy<n and graph[ix][iy] == 0):
          graph[ix][iy] = graph[x][y]
          queue.append((graph[ix][iy], ix, iy))
    cnt += 1
  return graph[X-1][Y-1]


virus.sort()
print(bfs(S,X,Y))