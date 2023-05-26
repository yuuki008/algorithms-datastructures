n = 6
G = [
[1, 2, 2, 3],
[2, 2, 3, 4],
[3, 1, 5],
[4, 1, 6],
[5, 1, 6],
[6, 0],
]

A = [[] for _ in range(n+1)]
def depth_first_search(v, time):
  if len(A[v]) > 0:
    return time

  # 初回訪問時刻
  time +=1
  A[v].append(v)
  A[v].append(time)

  for num in sorted(G[v-1][2:]):
    time = depth_first_search(num, time)

  # 隣接リスト探索完了時刻
  time += 1
  A[v].append(time)
  return time

time = 0
for g in G:
  time = depth_first_search(g[0], time)

for a in A:
  print(a)