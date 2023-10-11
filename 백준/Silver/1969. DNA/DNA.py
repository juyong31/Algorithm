# 각 문자열 입력
# 문자열의 한 자리씩 모든 문자열을 검사하는데, 자리가 바뀔 때 마다 A = 0, T = 0, G = 0, C = 0
# 모든 문자열의 해당자리를 돌면서, 각 문자열에 +1
# 가장 큰 값이 그 자리에 확정
# 그 외 문자의 숫자들은 모두 hamming Distance합에 추가

n, m = map(int, input().split())
arr = []
for _ in range(n):
  arr.append(list(map(str, input())))
res = ''
hammingDis = 0

for i in range(m):
  A = 0
  T = 0
  G = 0
  C = 0
  for j in range(n):
    if(arr[j][i] == 'T'):
      T += 1
    elif(arr[j][i] == 'A'):
      A += 1
    elif(arr[j][i] == 'G'):
      G += 1
    elif(arr[j][i] == 'C'):
      C += 1
  if(max(A,T,G,C) == A):
    res += 'A'
    hammingDis += T + G + C
  elif(max(A,T,G,C) == C):
    res += 'C'
    hammingDis += A + T + G
  elif(max(A,T,G,C) == G):
    res += 'G'
    hammingDis += A + T + C
  elif(max(A,T,G,C) == T):
    res += 'T'
    hammingDis += A + G + C

print(res)
print(hammingDis)