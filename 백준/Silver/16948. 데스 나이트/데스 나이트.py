# 이동할 수 있는 위치정보를 dx,dy로 저장해둠
# 각 queue에는 x,y,cnt(이동횟수) 가 들어감
# x==r2, y==c2 일때 cnt를 print, exit(0)
# 끝까지 bfs를 돌고 빠져나오면 print(-1)

from collections import deque

n = int(input())
graph = [[0]*n for _ in range(n)]
r1, c1, r2, c2 = map(int, input().split())
dx = [-2,-2,0,0,2,2]
dy = [-1,1,-2,2,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y,0))
    graph[x][y] = 1
    
    while queue:
        ix, iy, cnt = queue.popleft()
        if(ix == r2 and iy == c2):
            print(cnt)
            exit(0)
        for v in range(6):
            kx = dx[v] + ix
            ky = dy[v] + iy
            if(0<=kx<n and 0<=ky<n and graph[kx][ky] == 0):
                graph[kx][ky] = 1
                queue.append((kx,ky,cnt+1))
    


bfs(r1,c1)
print(-1)