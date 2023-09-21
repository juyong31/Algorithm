# x = dp[i]+dp[i-1], y = dp[i-1]+dp[i-2]
# 두개 곱

n = int(input())
dp = [0 for _ in range(81)]
dp[1] = 1
dp[2] = 1
dp[3] = 2
if(n==1):
  print(4)
elif(n==2):
  print(6)
elif(n==3):
  print(10)
else:
  for i in range(4, 81):
    dp[i] = dp[i-1]+dp[i-2]
  
  print((dp[n]+dp[n-1]+dp[n-1]+dp[n-2])*2)