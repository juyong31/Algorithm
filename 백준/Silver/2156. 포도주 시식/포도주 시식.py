n = int(input())

dp = [0]
total = [0 for _ in range(n+1)]
for _ in range(n):
  dp.append(int(input()))

if(n == 1):
  print(dp[1])
elif(n == 2):
  print(dp[1]+dp[2])
elif(n == 3):
  print(max(dp[1]+dp[2], dp[2]+dp[3], dp[1]+dp[3]))
else:
  total[1] = dp[1]
  total[2] = dp[1]+dp[2]
  total[3] = max(dp[1]+dp[2], dp[2]+dp[3], dp[1]+dp[3])
  
  for i in range(4, n+1):
    total[i] = max(total[i-2]+dp[i], total[i-3]+dp[i-1]+dp[i], total[i-1])

  print(total[n])