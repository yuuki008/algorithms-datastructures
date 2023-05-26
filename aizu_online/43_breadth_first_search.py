n = 6
G = [
[1, 2, 2, 4],
[2, 1, 5],
[3, 2, 5, 6],
[4, 0],
[5, 1, 4],
[6, 1, 6],
]

D = [-1 for _ in range(n+1)]
Q = [G[0][0]]
D[1] = 0
while len(Q):
  u = Q.pop(0)
  for v in sorted(G[u-1][2:]):
    if D[v] == -1:
      D[v] = D[u] + 1
      Q.append(v)

for i in range(1, len(D)):
  print(i, D[i])