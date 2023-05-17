n = 9
A = [
[0, 1, 4],
[1, 2, 3],
[2, -1, -1],
[3, -1, -1],
[4, 5, 8],
[5, 6, 7],
[6, -1, -1],
[7, -1, -1],
[8, -1, -1]
]

T = [{ 'parent': -1, 'degree': 0, 'type': 'root', 'height': 0, 'sibling': -1 } for _ in range(n)]

for i in range(n):
  T[A[i][0]]['node'] = A[i][0]
  T[A[i][0]]['childs'] = A[i][1:]
  if A[i][1] != -1:
    T[A[i][1]]['sibling'] = A[i][2]
  if A[i][2] != -1:
    T[A[i][2]]['sibling'] = A[i][1]
  if A[i][1] != -1:
    T[A[i][1]]['parent'] = A[i][0]
    T[A[i][0]]['degree'] += 1
  if A[i][2] != -1:
    T[A[i][2]]['parent'] = A[i][0]
    T[A[i][0]]['degree'] += 1
  if A[i][1] != -1 and A[i][2] != -1:
    T[A[i][0]]['type'] = 'leaf'

def find_depth(t, depth):
  if t['parent'] == -1:
    return depth

  return find_depth(T[t['parent']], depth + 1)

def find_height(node, height):
  if T[node]['degree'] == 0:
    return height

  max_height = height
  for child in T[node]['childs']:
    max_height = max(find_height(child, height + 1), max_height)
  return max_height

for t in T:
  depth = find_depth(t, 0)
  height = find_height(t['node'], 0)
  t['depth'] = depth
  t['height'] = height
  if depth == 0:
    t['type'] = 'root'
  elif t['degree'] == 0:
    t['type'] = 'leaf'
  else:
    t['type'] = 'internal node'

for t in T:
  print(f'node {t["node"]}: parent = {t["parent"]}, sibling = {t["sibling"]}, degree = {t["degree"]}, depth = {t["depth"]}, height = {t["height"]}, {t["type"]}')