# 최소 치환 횟수이기 때문에, 
# visited 값을 False로 초기화 후
# 하나의 위치에 방문할 때 마다 위치값 += 1
# 방문하는 위치가 b이면서 False이면 그 전위치값 +1을 출력

from collections import deque

a, b = map(int, input().split())
n, m = map(int, input().split())
arr = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for _ in range(m):
    x,y = map(int,input().split())
    arr[x].append(y)
    arr[y].append(x)
    
def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = 0
    
    while queue:
        current = queue.popleft()
        if(current == b):
            print(visited[current])
            exit(0)
        for v in arr[current]:
            if(visited[v] == False):
                visited[v] = visited[current] + 1
                queue.append(v)

bfs(a)
print(-1)