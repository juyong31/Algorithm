N = int(input())

if(N < 10):
  N = N*10
  
init = N
count = 0

while(True):
  first = N // 10
  last = N % 10
  
  res = first + last
  N = last * 10 + res % 10 
  count = count+1

  if(init == N):
    break

print(count)