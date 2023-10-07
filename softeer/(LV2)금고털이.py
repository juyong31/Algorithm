# 귀금속 당 가치를 구하고, 그 가치가 가장 높은 애부터 가방에 담기
# 가방에 담을 때는, 그 귀금속을 최대로 담는데,
# 가방의 빈 공간이 귀금속 총 용량보다 더 클경우엔 귀금속 크기만큼 담기
# 가방의 빈 공간이 귀금속의 총 용량보다 더 작을 경우엔 가방 여유공간 크기만큼 담기

w, n = map(int, input().split())
total_value = 0
bank = []
for _ in range(n):
  a, b = map(int, input().split())
  bank.append([a,b])
  
bank.sort(key = lambda bank :bank[1], reverse=True) # 무게당 가치가 높은 순으로 정렬


for i in range(n):
  if(bank[i][0] <= w): # 빈 공간이 더 큰경우 (귀금속이 있는만큼 다 가방에 넣는 경우)
    total_value += bank[i][0]*bank[i][1]
    w = w-bank[i][0]
  else: # 빈 공간이 귀금속 무게보다 더 작은 경우 (빈 공간 만큼 귀금속을 잘라서 넣는 경우)
    total_value += w * bank[i][1]
    break
  
print(total_value)