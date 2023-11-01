# visited = 0~100000까지 만듬
# 시작위치 = 1
# bfs(n) 호출
# -1, +1, +a, +b, -a, -b, a배, b배를 각각 구해서
# for문을 8번 수행해서, 각 경우를 if문으로 조사
# if문으로 했을 때, 해당 위치가 False면 이전 숫자 +1 지정
# 숫자가 m이면 visited값 반환

from collections import deque

a, b, n, m = map(int, input().split())
visited = [False for _ in range(100001)]

def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = 0
    
    while queue:
        current = queue.popleft()
        index = [current-1, current+1, current+a, current-a, current+b, current-b, current*a, current*b]
        for v in range(8):
            nextNum = index[v]
            if(0 <= nextNum <= 100000 and visited[nextNum] == False):
                visited[nextNum] = visited[current] + 1
                queue.append(nextNum)
                if(nextNum == m):
                    print(visited[nextNum])
                    exit(0)

bfs(n)