# 한 번에 들 수 있는 책 수가 M이고, 마지막에는 돌아오지 않아도 됨
# 즉, 마지막에는 젤 먼곳에 가는것이 효율적
# -와 +를 리스트에 나누어서 넣어야함
# plus = reversed true, minus = sort
# 각 리스트 책위치를 수행할 때, M으로 나눴을 때 큰 값부터 M씩 이동하며 res에 +
# 수행 후 res 값에 * 2
# abs plus len 과 abs minus len 을 비교하여 더 큰 숫자를 마지막에 빼줌(왕복안하고 종료)

n, m = map(int, input().split())
arr = list(map(int, input().split()))
plus = []
minus = []
res = 0
maxNum = 0
for v in arr:
  if(v > 0):
    plus.append(v)
  else:
    minus.append(v)
  if abs(v) > abs(maxNum): # 최대값을 구하기 위해
    maxNum = v

plus.sort(reverse = True)
minus.sort()

for i in range(0, len(minus), m):
  res += abs(minus[i])

for j in range(0, len(plus), m):
  res += plus[j]

res *= 2

res -= abs(maxNum)

print(res)