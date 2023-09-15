import sys
sys.setrecursionlimit(10000)

dx = [1, 1, 0, -1, -1, -1, 0, 1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
result = []

def dfs(x,y):
    graph[x][y] = 0
    
    for k in range(8):
        index_x = dx[k] + x
        index_y = dy[k] + y
        if(0 <= index_x < h and 0 <= index_y < w and graph[index_x][index_y] == 1):
            dfs(index_x, index_y)

while True:
    graph = []
    cnt = 0
    
    w, h = map(int, input().split())
    if(w == 0 and h == 0):
        break
    
    for i in range(h):
        graph.append(list(map(int, input().split())))
        
    for i in range(h):
        for j in range(w):
            if(graph[i][j] == 1):
                dfs(i, j)
                cnt += 1
    
    result.append(cnt)
            
for z in result:
    print(z)