# 정렬 후, 가장 중간 값을 찾는 것이 핵심
# 홀수인 경우 문제없지만
# 짝수인 경우 2개의 중간 값 중 왼쪽값이 선택되어야 함

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
print(arr[(n-1)//2]) # 1을빼서 짝수인 경우 2개의 중간 값 중 왼쪽값이 선택되게 해줌