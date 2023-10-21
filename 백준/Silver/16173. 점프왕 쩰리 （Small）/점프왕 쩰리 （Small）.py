# bfs로 목적지에 도착하는지 확인
# 방문한곳은 False로 변경

from collections import deque

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    
    while queue:
        ix, iy = queue.popleft()
        dx = [graph[ix][iy], 0]
        dy = [0, graph[ix][iy]]
        if(graph[ix][iy] == -1):
            print('HaruHaru')
            exit(0)
        graph[ix][iy] = False
        for v in range(2):
            kx = ix + dx[v]
            ky = iy + dy[v]
            if(0 <= kx < n and 0 <= ky < n and graph[kx][ky] != False):
                queue.append((kx,ky))
    

bfs(0,0)
print('Hing')