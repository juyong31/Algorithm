import sys
sys.setrecursionlimit(100000)

n, m = map(int, input().split())

graph = []
dx = [0,0,1,-1]
dy = [1,-1,0,0]
dp = [[-1]*m for _ in range(n)]
for _ in range(n):
  graph.append(list(map(int, input().split())))
  
def dfs(x,y):
  if(x == n-1 and y == m-1):
    return 1
  
  if(dp[x][y] == -1):
    dp[x][y] = 0
    
    for v in range(4):
      ix = dx[v] + x
      iy = dy[v] + y
      if(0 <= ix < n and 0 <= iy < m and graph[ix][iy] < graph[x][y]):
        dp[x][y] += dfs(ix, iy)
      
  return dp[x][y]

  
total = dfs(0,0)
print(total)