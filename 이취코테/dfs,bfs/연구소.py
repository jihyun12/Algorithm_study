n,m= map(int,input().split())
graph = []
temp = [[0]*m for _ in range(n)]
safety=0

for i in range(n):
  graph.append(list(map(int,input().split())))

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def virus(x,y):
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]

      if nx>=0 and ny>=0 and nx<n and ny<m:
        if temp[nx][ny]==0:
          temp[nx][ny] = 2
          virus(nx,ny)

def safe():
  num=0
  for i in range(n):
    for j in range(m):
      if temp[i][j] == 0:
        num += 1
  return num

def dfs(count):
  global safety
  if count == 3:
    for i in range(n):
      for j in range(m):
        temp[i][j]=graph[i][j]
      
    for i in range(n):
      for j in range(m):
        if temp[i][j]== 2:
          virus(i,j)
    safety = max(safety,safe())
    return

  for i in range(n):
    for j in range(m):
      if graph[i][j] == 0:
        graph[i][j] =1
        count += 1
        dfs(count)
        graph[i][j]=0
        count -= 1

dfs(0)
print(safety)


