n, k = map(int, input().split())
arr = [[0,0]]
for _ in range(n):
  w,v = map(int, input().split())
  arr.append([w,v])
  
dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(1, n+1):
  weight = arr[i][0]
  value = arr[i][1]
  for j in range(1,k+1):
    if(j < weight):
      dp[i][j] = dp[i-1][j]
    else:
      dp[i][j] = max(dp[i-1][j-weight]+value, dp[i-1][j])
    
print(dp[n][k])