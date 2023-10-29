from collections import deque

n, m = map(int, input().split())

graph = []
dx = [1,1,0,-1,-1,-1,0,1]
dy = [0,1,1,1,0,-1,-1,-1]
cnt = 0
for _ in range(n):
    graph.append(list(map(int, input().split())))

def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    graph[i][j] = 0
    
    while queue:
        ix, iy = queue.popleft()
        for v in range(8):
            kx = dx[v] + ix
            ky = dy[v] + iy
            if(0 <= kx < n and 0 <= ky < m and graph[kx][ky] == 1):
                queue.append((kx, ky))
                graph[kx][ky] = 0


for i in range(n):
    for j in range(m):
        if(graph[i][j] == 1):
            bfs(i, j)
            cnt += 1
            
            
print(cnt)