# 삼각형 만드려면, 2개 변의 합이 나머지하나보다 커야함
import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort(reverse=True)
res = -1

for i in range(0, len(arr)-2):
    if(arr[i] < arr[i+1] + arr[i+2]):
        res = arr[i]+arr[i+1]+arr[i+2]
        break
        
print(res)