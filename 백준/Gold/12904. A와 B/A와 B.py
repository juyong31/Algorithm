# A 에서 B까지 가는 것이 아닌, B 에서 A 를 가는 방식 수행

S = list(input())
T = list(input())

while T:
  if(T[-1] == 'A'):
    T.pop()
  elif(T[-1] =='B'):
    T.pop()
    T.reverse()
  if(S == T):
    print(1)
    exit(0)

print(0)