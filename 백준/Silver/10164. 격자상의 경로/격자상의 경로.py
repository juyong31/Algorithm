# k가 0인경우와 그렇지 않은 경우로 구분
# k = 0이면 dp[n][m]까지 2중 for문으로 구하면 됨 (dp[i][j] = dp[i-1][j]+dp[i][j-1])
# k != 이면 0~k까지의 경우의 수 * k~끝까지의 경우의 수

n, m, k = map(int, input().split())
dp = [[0]*(m) for _ in range(n)]

# k == 0 이면, 목표지점에 도착하는 총 경우의 수 출력
if(k == 0):
  for i in range(n):
    for j in range(m):
      if(i == 0 or j == 0):
        dp[i][j] = 1
      else:
        dp[i][j] = dp[i-1][j]+dp[i][j-1]
  print(dp[n-1][m-1])

# k != 0 이면, (k까지의 거리까지 경우의 수)*(k~최종 거리까지 경우의 수)
else:
  # k의 위치를 x, y 좌표로 나타내기
  x = (k-1) // m
  y = (k-1) % m

  # [0][0]에서 k까지의 경우의 수
  for i in range(x+1):
    for j in range(y+1):
      if(i == 0 or j == 0):
        dp[i][j] = 1
      else:
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

  res1 = dp[x][y]

  # k에서 n,m까지의 경우의 수
  for i in range(x, n):
    for j in range(y, m):
      if(i == x and j == y):
        continue
      if(i == x or j == y): # k~[n][m]까지 구하기 위해 가장 바깥쪽 dp값 1로 초기화
        dp[i][j] = 1
      else:
        dp[i][j] = dp[i-1][j]+dp[i][j-1]
  res2 = dp[n-1][m-1]

  print(res1*res2)