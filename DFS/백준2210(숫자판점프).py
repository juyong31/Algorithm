graph = [list(map(str, input().split())) for _ in range(5)]
res = []
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(x,y,number):
  if(len(number) == 6):
    if(number not in res):
      res.append(number)
    return

  for v in range(4):
    ix = dx[v] + x
    iy = dy[v] + y
    if(0 <= ix < 5 and 0 <= iy < 5):
      dfs(ix, iy, number + graph[ix][iy])



for i in range(5):
  for j in range(5):
    dfs(i,j,graph[i][j])

print(len(res))
