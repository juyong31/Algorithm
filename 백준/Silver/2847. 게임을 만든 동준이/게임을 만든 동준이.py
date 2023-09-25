# 리스트 뒤에서부터 0까지 돌면서, 뒷쪽 숫자가 앞쪽 숫자보다 클때까지 앞쪽숫자 -, cnt+

n = int(input())
arr = []
for _ in range(n):
  arr.append(int(input()))

cnt = 0
for i in range(n-1, 0, -1):
  if(arr[i] <= arr[i-1]):
    while(arr[i] <= arr[i-1]):
      arr[i-1] -= 1
      cnt += 1
      
print(cnt)