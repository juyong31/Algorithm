# 첫번째 숫자와 두번째 숫자의 관계를 통해 ascending인지 descending인지 기준 설정
# 나머지 숫자를 쭉 돌면서 기준에 어긋나면 mixed 출력 후 종류
# 기준따라 끝까지가면 기준 출력

arr = list(map(int, input().split()))

if(arr[0] > arr[1]):
  res = 'descending'
  for i in range(len(arr)-1):
    if(arr[i] < arr[i+1]):
      print('mixed')
      exit(0)
    
else:
  res = 'ascending'
  for i in range(len(arr)-1):
    if(arr[i] > arr[i+1]):
      print('mixed')
      exit(0)
      
print(res)