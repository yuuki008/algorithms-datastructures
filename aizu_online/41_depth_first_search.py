n = 3
adj = [
[1, 1, 2],
[2, 1, 3],
[3, 1, 1]
]
A = [[] for _ in range(n+1)]
def depth_first_search(v, time):
  if len(A[v]) > 0:
    return time

  time += 1
  A[v].append(v)
  A[v].append(time)
  V = sorted(adj[v-1][2:])
  for num in V:
    if num == v:
      continue
    time = depth_first_search(num, time)
  time += 1
  A[v].append(time)
  return time


time = 0
for i in range(n):
  time = depth_first_search(adj[i][0], time)

for a in A[1:]:
  print(*a)