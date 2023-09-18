n = int(input())

dp = []

for _ in range(n):
  dp.append(list(map(int, input().split())))

if(n == 1):
  print(dp[0][0])
elif(n == 2):
  print(max(dp[0][0]+dp[1][0], dp[0][0]+dp[1][1]))
else:
  dp[1][0] = dp[0][0] + dp[1][0]
  dp[1][1] = dp[0][0] + dp[1][1]
  
  for i in range(2, n):
    length = len(dp[i])
    dp[i][0] = dp[i-1][0] + dp[i][0]
    dp[i][length-1] = dp[i-1][length-2] + dp[i][length-1]
    for j in range(1,length-1):
      dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + dp[i][j]
  print(max(dp[n-1]))