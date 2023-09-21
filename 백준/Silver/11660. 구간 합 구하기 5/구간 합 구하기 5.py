# 0~i, 0~j 까지 합을 dp[i][j]에 누적 저장하는 dp 생성
# 특정 좌표가 주어지면, 그 위치까지의 총합 - 시작점~그 위치 시작점 + 겹치는부분
# **코드에서 graph = [0][0]에서부터 시작하고, dp = [1][1]부터 시작함
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int, input().split())))
dp = [[0]*(n+1) for _ in range(n+1)]


# dp 풀셋팅
for i in range(1, n+1):
  for j in range(1, n+1):
    dp[i][j] = dp[i-1][j] + dp[i][j-1] + graph[i-1][j-1] - dp[i-1][j-1]
    
# dp[x2][y2]의 값에서 [x1][y1]보다 작은 부분에 해당하는 값을 빼준 후, 겹치는 부분 +
for _ in range(m):
  x1,y1,x2,y2 = map(int, input().split())
  print(dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1])