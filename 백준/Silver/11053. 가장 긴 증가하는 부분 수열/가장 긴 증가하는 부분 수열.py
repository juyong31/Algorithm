a = int(input())
arr = list(map(int, input().split()))
dp = [1 for _ in range(a)]

for i in range(len(arr)):
  for j in range(i):
    if(arr[i] > arr[j]):
      dp[i] = max(dp[i], dp[j]+1)
      

print(max(dp))