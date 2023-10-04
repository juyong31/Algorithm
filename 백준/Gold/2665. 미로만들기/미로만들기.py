# bfs로 방문하지 않은 항목을 찾는다
# 방문하지 않은 항목 중, 1(흰색)인 경우 appendleft, 0(검정)인 경우 append 한다. 이를통해 흰색인 경우를 가장 우선적으로 탐색

from collections import deque

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))
visited = [[-1]*n for _ in range(n)] # visited는 뚫은 벽 개수저장/방문여부체크 두가지 목적
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs():
    visited[0][0] = 0 #뚫은개수 0
    queue = deque()
    queue.append((0,0))
    
    while queue:
        x, y = queue.popleft()
        if(x == n-1 and y == n-1):
            break
        for v in range(4):
            ix = x + dx[v]
            iy = y + dy[v]
            if(0 <= ix < n and 0 <= iy < n and visited[ix][iy] == -1):
                if(graph[ix][iy] == 1): # 방문하지 않은 지역 중 1인곳은, 벽을 뚫은 횟수를 추가할 필요가 없음
                    visited[ix][iy] = visited[x][y]
                    queue.appendleft((ix,iy)) # 검정색보다 흰색만 우선적으로 고려하기 위해 appendleft
                else: # 방문하지 않은 지역 중 0인곳은, 벽을 뚫어야 하는 횟수를 더해서 저장
                    visited[ix][iy] = visited[x][y]+1
                    queue.append((ix,iy)) 
        
    return visited[n-1][n-1]

        
print(bfs())