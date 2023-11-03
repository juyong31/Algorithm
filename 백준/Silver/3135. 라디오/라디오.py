# N개의 숫자를 각각 list에 넣는데,
# 넣을 때 B-number 한 상태로 넣어야함
# minNum = min(list)
# minNum과 B-A+1 중 더 작은 수 출력

a, b = map(int, input().split())

arr = []
n = int(input())
for _ in range(n):
    index = int(input())
    arr.append(abs(b-index))

minNum = min(arr)

if(minNum+1 < abs(b-a)):
    print(minNum+1)
else:
    print(abs(b-a))