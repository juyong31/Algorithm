# knapsack 배낭 문제와 비슷
# 100이상이면 안되기 때문에, dp[n][99]

n = int(input())

energy = [0] + list(map(int, input().split()))
happy = [0] + list(map(int, input().split()))
dp = [[0]*(101) for _ in range(n+1)]


for i in range(1, n+1):
  for j in range(1, 101):
    if(j >= energy[i]):
      dp[i][j] = max(dp[i-1][j], dp[i-1][j-energy[i]]+happy[i])
    else:
      dp[i][j] = dp[i-1][j]

print(dp[n][99])