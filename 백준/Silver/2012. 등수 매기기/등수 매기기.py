# sort 후 각 자리에 맞는 수까지 +1, cnt+1

import sys
input = sys.stdin.readline

n = int(input())
arr = [0]
for _ in range(n):
  arr.append(int(input()))

arr.sort()
cnt = 0
for i in range(1, n+1):
  cnt += abs(arr[i]-i)


print(cnt)