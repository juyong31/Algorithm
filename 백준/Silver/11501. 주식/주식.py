# 역으로 조사를 하는데, maxNum보다 큰 number가 있으면, 그 숫자를 만나기 전까지 숫자들을 maxNum에 팔아버리고
# maxNum은 새로운 숫자로 지정

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    indexArr = []
    res = 0

    maxNum = arr[n-1]
    for i in range(n-2, -1, -1):
        if(arr[i] > maxNum):
            for j in indexArr:
                res += maxNum - j
            maxNum = arr[i]
            indexArr = []
        elif(arr[i] < maxNum):
            indexArr.append(arr[i])

    if(len(indexArr) > 0):
        for k in indexArr:
            res += maxNum - k
        
    print(res)