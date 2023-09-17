t = int(input())
arr = []
for k in range(t):
  n = int(input())
  
  dp = [0] * (n+1)
  if(n == 1):
    arr.append(1)
  elif(n == 2):
    arr.append(2)
  elif(n == 3):
    arr.append(4)
  else:
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    
    for i in range(4, n+1):
      dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
    
    arr.append(dp[n])

for v in arr:
  print(v)