# 상자 개수만큼 for 문을 돌림
# 각 숫자마다 그 숫자까지 for 문을 돌림
# i가 j 보다 클 경우, max(dp[i], dp[j]+1)

n = int(input())
arr = list(map(int, input().split()))
dp = [1 for _ in range(n)]

for i in range(1, n):
  for j in range(i):
    if(arr[i] > arr[j]):
      dp[i] = max(dp[i], dp[j]+1)
print(max(dp))