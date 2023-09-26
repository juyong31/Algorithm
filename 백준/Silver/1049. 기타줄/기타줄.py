# 1개짜리끼리 비교해서 가장 가성비좋은 브랜드 선택
# 패키지끼리 비교해서 가장 가성비좋은 브랜드 선택
# package 가성비가 each보다 더 좋을경우, 6미만으로 남았을 때 package가격과 each가격 추가로 고려해야함

n,m = map(int, input().split())
package = 1000
each = 1000

for _ in range(m):
  a, b = map(int, input().split())
  if(a < package):
    package = a
  if(b < each):
    each = b

if(package/6 <= each):
  res = (n//6*package) + ((n%6)*each)
  if(package < each*(n%6)):
    res = package*(n//6 + 1)
  

  print(res)
  
else:
  print(each*n)