# 양수 list와 음수&0 list 생성, 1일 경우엔 result에 바로 +
# 각각의 list sort (양수list는 reverse)
# list별로 묶으면서 계산을하는데, 1개남았을때는 +


n = int(input())
plus = []
minus = []
res = 0

for _ in range(n):
    number = int(input())
    if(number > 1):
        plus.append(number)
    elif(number <= 0):
        minus.append(number)
    else: # number == 1인경우
        res += number
        
plus.sort(reverse=True)
minus.sort()


# 양수list 계산
for i in range(0, len(plus), 2):
    if(i+1 >= len(plus)):
        res += plus[i]
    else:
        res += (plus[i]*plus[i+1])
        
# 음수list 계산
for j in range(0, len(minus), 2):
    if(j+1 >= len(minus)):
        res += minus[j]
    else:
        res += (minus[j]*minus[j+1])
        
print(res)