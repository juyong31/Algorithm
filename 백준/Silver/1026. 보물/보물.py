N = int(input())

arrA = list(map(int, input().split()))
arrB = list(map(int, input().split()))

arrA.sort()
total = 0


for i in range(N):
  total += arrA[i] * max(arrB)
  arrB.remove(max(arrB))

print(total)