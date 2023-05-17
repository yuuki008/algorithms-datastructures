
n = 4
A = [
[0, 0],
[1, 3, 2, 3, 0],
[2, 0],
[3, 0]
]

T = [{'parent': -1} for _ in range(n)]

for i in range(n):
  T[A[i][0]]['node'] = A[i][0]
  T[A[i][0]]['childs'] = A[i][2:]
  for j in T[A[i][0]]['childs']:
    T[j]['parent'] = A[i][0]

def recursive(t, depth):
  if t['parent'] == -1:
    return depth

  return recursive(T[t['parent']], depth+1)

for t in T:
  depth = recursive(t, 0)
  if depth == 0:
    t['type'] = 'root'
  elif len(t['childs']) == 0:
    t['type'] = 'leaf'
  else:
    t['type'] = 'internal node'
  t['depth'] = depth



for t in T:
  print(f'node {t["node"]}: parent = {t["parent"]}, depth = {t["depth"]}, {t["type"]}, {t["childs"]}')