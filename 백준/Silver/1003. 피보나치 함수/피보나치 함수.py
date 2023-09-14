zero = [1,0,1]
one = [0,1,1]
index = []

def fibo(num):
  length = len(zero)
  if(num >= length):
    for i in range(length, num+1):
      zero.append(zero[i-2] + zero[i-1])
      one.append(one[i-2] + one[i-1])
  
  index.append([zero[num], one[num]])

t = int(input())
for k in range(t):
  number = int(input())
  fibo(number)

for x,y in index:
  print(x, y)