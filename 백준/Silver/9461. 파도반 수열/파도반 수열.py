t = int(input())
arr = []

for _ in range(t):
  n = int(input())

  dp = [0 for _ in range(n+1)]
  if(n == 1):
    arr.append(1)
  elif(n == 2):
    arr.append(1)
  elif(n == 3):
    arr.append(1)
  else:
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    
    for i in range(4, n+1):
      dp[i] = dp[i-2]+dp[i-3]
    
    arr.append(dp[n])
    
for v in arr:
  print(v)