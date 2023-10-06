# 입력값을 bfs를 돌리는데
# 각 자리수별로 +1, %10 (각 자리별로 0~9까지 경우의수 구하기 위해)
# 그렇게 했을 때 소수이면 queue에 추가, cnt += 1
# 이렇게 while 돌다가 B값과 같으면 return cnt

from collections import deque
import math

# 소수판별
def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임


def bfs(start, startcnt):
  queue = deque()
  queue.append((start, startcnt)) # cnt를 함께 저장해서, 각 숫자까지 도달하는 횟수 저장
  visited = [0 for i in range(10000)] # 방문여부 확인
  visited[start] = 1

  while queue:
    number, cnt = queue.popleft()
    currentNum = str(number)
    if(number == b):
      return cnt
    for i in range(4):
      for j in range(10):
        tempNum = int(currentNum[:i] + str(j) + currentNum[i+1:]) # 각 자리별로 구하기 위해
        primeindex = is_prime_number(tempNum)
        if(visited[tempNum] == 0 and primeindex == True and tempNum >= 1000):
          visited[tempNum] = 1
          queue.append((tempNum, cnt+1))


n = int(input())
for _ in range(n):
  a, b = map(int, input().split())
  print(bfs(a, 0))