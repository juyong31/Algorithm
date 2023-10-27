# start값과 end값을 list에 저장
# heap 형태로 end시간을 관리함
# heapq > arr[i][0] 이면 heapq.heappush
# else이면 heapq.heappop, heappush

import heapq

n = int(input())
arr = []
currentList = []

for _ in range(n):
  arr.append(list(map(int, input().split())))

arr.sort(key = lambda x : x[1])# 시작시간으로 정렬

heapq.heappush(currentList, arr[0][2])
for i in range(1, n):
  if(arr[i][1] < currentList[0]):
    heapq.heappush(currentList, arr[i][2])
  else:
    heapq.heappop(currentList)
    heapq.heappush(currentList, arr[i][2])


print(len(currentList))