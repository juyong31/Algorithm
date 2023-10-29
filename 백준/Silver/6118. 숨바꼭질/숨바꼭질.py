# 연결되어 있는 상태를 나타내는 list 1개
# 각 헛간별로, 1에서 도달하는데까지 걸리는 거리 저장할 list 1개

from collections import deque

n, m = map(int, input().split())
visited = [0]*(n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = 1
    
    while queue:
        current = queue.popleft()
        for i in graph[current]:
            if(visited[i] == 0):
                visited[i] = visited[current] + 1
                queue.append(i)    


bfs(1)
maxNum = max(visited)
print(visited.index(maxNum), maxNum-1, visited.count(maxNum))