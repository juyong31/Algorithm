# top -> bottom 방식 (결과를가지고 시작값을 만들기)
# 10으로 나눠주는것(나머지가 1인경우)이 2로 나누는 것보다 연산효율을 줄임
# 두개 다 불가능할 경우 만들수 없는 것으로 판단

a, b = map(int, input().split())

cnt = 1
while a != b:
    tmp = b #if문 중 하나도 거치지 않았을 경우 비교를 위해
    if(b%10 == 1):
        b = b//10
        cnt += 1
    elif(b%2 == 0):
        b = b//2
        cnt += 1
    
    if(tmp == b): #if문을 하나도 거치지 않은 경우
        cnt = -1
        break

if(cnt == -1):
    print(-1)
else:
    print(cnt)