# 각 문자열을 비교해서
# 더 큰 개수를 출력

t = int(input())
for _ in range(t):
  n = int(input())
  str1 = str(input())
  str2 = str(input())
  
  black = 0
  white = 0
  cnt = 0
  
  for i in range(len(str1)):
    if(str1[i] != str2[i]):
      if(str1[i] == 'B'):
        black += 1
      else:
        white += 1
  
  if(black >= white):
    print(black)
  else:
    print(white)