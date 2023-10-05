# 상하좌우를 조사해서, L이상 R이하 차이난다면, True로 변경
# visited에는 방문여부를 체크해주고 (bfs 들어가기전에 항상 초기화)
# temp는 bfs결과 리스트를 가지고 나옴 (bfs 들어가기전에 항상 초기화)

from collections import deque
import sys
input = sys.stdin.readline

n, l, r = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
dx = [0,0,1,-1]
dy = [1,-1,0,0]
res = 0


# bfs. l이상 r이하인 경우 temp에 담아줄예정
def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    temp.append((x,y))
    visited[x][y] = True
    
    while queue:
        ix,iy = queue.popleft()
        for v in range(4):
            kx = ix+dx[v]
            ky = iy+dy[v]
            if(0<=kx<n and 0<=ky<n and visited[kx][ky] == False):
                if(l <= abs(graph[ix][iy]-graph[kx][ky]) <= r):
                    queue.append((kx,ky))
                    temp.append((kx,ky))
                    visited[kx][ky] = True

# 바꿀 도시가 있을경우 계속 수행하는 while문
# bfs 리턴결과를 가지고 평균을 하여 graph 값을 바꿔주는 역할
while True:
    visited = [[False]*n for _ in range(n)]
    flag = 0
    
    for i in range(n):
        for j in range(n):
            if(visited[i][j] == False):
                temp = []
                bfs(i,j)
                if(len(temp) > 1):
                    flag = 1               
                    number = sum([graph[x][y] for x,y in temp]) // len(temp)
                    for x,y in temp:
                        graph[x][y] = number
                    

    if(flag == 0):
        break
    else:
        res += 1
    

print(res)