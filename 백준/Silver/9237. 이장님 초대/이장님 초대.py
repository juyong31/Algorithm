n = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
maxNum = arr[0]

if n == 1:
    print(n+2)
else:
    for i in range(1, n):
        if maxNum < (i+arr[i]):
            maxNum = i+arr[i]
    
    print(maxNum+2)