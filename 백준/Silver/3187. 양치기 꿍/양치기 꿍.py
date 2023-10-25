# #이 아닐경우 v와 k의 개수를 초기화 후,  bfs를 수행
# v와 k의 개수를 비교

from collections import deque

r, c = map(int, input().split())
total_sheep = 0
total_wolf = 0
dx = [0,0,1,-1]
dy = [1,-1,0,0]
visited = [[False]*c for _ in range(r)]

graph = []
for _ in range(r):
    graph.append(list(input()))
    
def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    wolf = 0
    sheep = 0
    visited[x][y] = True
    
    while queue:
        ix, iy = queue.popleft()
        if(graph[ix][iy] == 'v'):
            wolf += 1
        elif(graph[ix][iy] == 'k'):
            sheep += 1
        graph[ix][iy] = '#'
        for t in range(4):
            kx = ix + dx[t]
            ky = iy + dy[t]
            if(0<=kx<r and 0<=ky<c and graph[kx][ky] != '#' and visited[kx][ky] == False):
                queue.append((kx,ky))
                visited[kx][ky] = True
    if(sheep > wolf):
        wolf = 0
    else:
        sheep = 0
    return wolf, sheep



for i in range(r):
    for j in range(c):
        if(graph[i][j] != '#'):
            a, b = bfs(i,j)
            total_wolf += a
            total_sheep += b
                
print(total_sheep, total_wolf)