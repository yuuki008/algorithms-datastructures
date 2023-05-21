
n = 6
A = [None, 10, 8, 5, 1, 2, 3]

for i in range(1, n + 1):
  node = i
  key = A[i]
  ans = f'node {node}: key = {key},'
  pk = A[i // 2]
  if pk is not None:
    ans += f' parent key = {pk},'
  if i * 2 <= n:
    ans += f' left key = {A[i*2]},'
  if i * 2 + 1 <= n:
    ans += f' right key = {A[i*2+1]},'
  print(ans)