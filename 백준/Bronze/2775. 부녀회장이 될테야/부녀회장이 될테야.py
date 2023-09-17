t = int(input())
arr = []

for v in range(t):
  k = int(input())
  n = int(input())
  
  dp = [[0]*(n+1) for _ in range(k+1)]
  for q in range(1, n+1):
    dp[0][q] = q
  
  for i in range(1, k+1):
    for j in range(1, n+1):
      for e in range(1, j+1):
        dp[i][j] += dp[i-1][e]

  arr.append(dp[k][n])

for p in arr:
  print(p)