# graph가 양방향이 아니라 단방향임
# distance list를 만들어서, distance값 비교

from collections import deque
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
visited = [False for _ in range(n+1)]
distance = [0 for _ in range(n+1)]
res = []


def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = True
    
    while queue:
        current = queue.popleft()
        for i in graph[current]:
            if(visited[i] == False):
                visited[i] = True
                distance[i] = distance[current] + 1
                queue.append(i)
                if(distance[i] == k):
                    res.append(i)

          
bfs(x)
if(len(res) == 0):
    print(-1)
else:
    res.sort()
    for k in res:
        print(k)