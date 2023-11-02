n = int(input())

arr = {}

for _ in range(n):
  index = input()
  if(index in arr):
    arr[index] += 1
  else:
    arr[index] = 1

maxNum = max(arr.values())

maxList = []

for key, value in arr.items():
  if(value == maxNum):
    maxList.append(key)

maxList = sorted(maxList)
print(maxList[0])