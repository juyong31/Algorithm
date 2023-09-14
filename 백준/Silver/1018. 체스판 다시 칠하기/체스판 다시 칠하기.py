N, M = map(int, input().split())

i = 0
j = 0
k = 0
l = 0
list1 = []
minNum = 1000000
for _ in range(N):
  index = str(input())
  list1.append(index)

for i in range(i, N-7):
  j = 0
  for j in range(j, M-7):
    changeCount = 0

    for k in range(8):
      for l in range(8):          
        if(((k+l)%2 == 0) or (k+l == 0)):
          if(list1[i+k][j+l] == 'W'):
            changeCount += 1
        else:
          if(list1[i+k][j+l] == 'B'):
            changeCount += 1
            
    if(minNum > changeCount):
      minNum = changeCount

    changeCount = 0
    
    for k in range(8):
      for l in range(8):
        if(((k+l)%2==0) or (k+l == 0)):
          if(list1[i+k][j+l] == 'B'):
            changeCount += 1
        else:
          if(list1[i+k][j+l] == 'W'):
            changeCount += 1
            
    if(minNum > changeCount):
      minNum = changeCount

print(minNum)
