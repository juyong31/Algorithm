n = int(input())

dp = []
total = [0] * n
for _ in range(n):
  dp.append(int(input()))
  
if(len(dp) <= 2):
  print(sum(dp))
else:
  total[0] = dp[0]
  total[1] = dp[0] + dp[1]
  total[2] = max(dp[0]+dp[2], dp[1]+dp[2])

  for i in range(3, n):
    total[i] = max(total[i-2]+dp[i], total[i-3]+dp[i-1]+dp[i])
    
  print(total[n-1])