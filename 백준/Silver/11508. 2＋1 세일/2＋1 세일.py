n = int(input())

arr = []
res = 0
for _ in range(n):
  arr.append(int(input()))


arr.sort(reverse = True)

for i in range(len(arr)):
  if(i%3 != 2):
    res += arr[i]
    
print(res)