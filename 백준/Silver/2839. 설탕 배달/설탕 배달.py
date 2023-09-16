N = int(input())

kg3 = 0
total = 0

while True:
  kg5 = 0
  while (((kg5*5)+(kg3*3))<=N):
    if((kg5*5)+(kg3*3) == N):
      total = kg5+kg3
      break
    kg5 += 1
    
  if(total != 0):
    print(total)
    break
    
  kg3 += 1
  
  if((kg3*3) > N):
    print(-1)
    break