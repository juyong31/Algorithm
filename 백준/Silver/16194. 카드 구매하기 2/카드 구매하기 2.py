n = int(input())
dp = [99999 for _ in range(n+1)]
arr = [0] + list(map(int, input().split()))
dp[0] = 0

for i in range(1, n+1):
  for j in range(1, i+1):
    dp[i] = min(dp[i], dp[i-j]+arr[j])

print(dp[n])