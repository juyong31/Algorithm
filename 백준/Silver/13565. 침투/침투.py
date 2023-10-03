# 젤 윗줄에 white(0) 있는지 확인해서 있으면 전류공급(2)
# bfs를 통해 흰색은 전부다 전류공급(2)
# bfs를 통해 전류공급을 마친 후,
# 젤 아랫줄에 공급된 전류(2)가 있는지 확인
# 있으면 YES, 없으면 NO
from collections import deque

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))
dx = [0,0,1,-1]
dy = [1,-1,0,0]


def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 2
    
    while queue:
        ix,iy = queue.popleft()
        for v in range(4):
            kx = dx[v] + ix
            ky = dy[v] + iy
            if(0 <= kx < n and 0 <= ky < m and graph[kx][ky] == 0):
                graph[kx][ky] = 2
                queue.append((kx,ky))


# 젤 윗줄에 white있는지 확인
for i in range(m):
    if(graph[0][i] == 0):
        bfs(0,i)

# 젤 아랫줄에 전류가 흐른 곳(2)이 있는지 확인
for j in range(m):
    if(graph[n-1][j] == 2):
        print('YES')
        exit(0)
print('NO')