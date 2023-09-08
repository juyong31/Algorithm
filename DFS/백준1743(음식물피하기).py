# 빈곳을 보면 울타리(#)로 변경
# 울타리가 아니면 죄다 dfs를 돌림
# 영역 내 양과 늑대 수 찾기

import sys
sys.setrecursionlimit(100000)

r, c = map(int, input().split())
graph = []
for _ in range(r):
  graph.append(list(input()))
total_wolf = 0
total_sheep = 0
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(graph, x, y):
  global sheep
  global wolf
  if(graph[x][y] == '.'):
    graph[x][y] = '#'
  elif(graph[x][y] == 'v'):
    wolf += 1
    graph[x][y] = '#'
  elif(graph[x][y] == 'o'):
    sheep += 1
    graph[x][y] = '#'
  
  for v in range(4):
    ix = dx[v] + x
    iy = dy[v] + y
    if(0 <= ix < r and 0 <= iy < c and graph[ix][iy] != '#'):
      dfs(graph, ix, iy)


for i in range(r):
  for j in range(c):
    if(graph[i][j] != '#'):
      sheep = 0
      wolf = 0
      dfs(graph,i,j)
      if(wolf != 0 or sheep != 0):
        if(wolf >= sheep):
          sheep = 0
        else:
          wolf = 0
      total_sheep += sheep
      total_wolf += wolf
      
print(total_sheep, total_wolf)