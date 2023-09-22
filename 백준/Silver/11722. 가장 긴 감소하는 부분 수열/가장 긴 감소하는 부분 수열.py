# 2중 for문을 돌리는데
# i < j 일경우, dp[i] = max(dp[i], dp[j]+1)

n = int(input())
arr = list(map(int, input().split()))
dp = [1 for i in range(n)]
cnt = 0
dp[0] = 1

for i in range(1, n):
  for j in range(i):
    if(arr[i]<arr[j]):
      dp[i] = max(dp[i], dp[j]+1)

print(max(dp))