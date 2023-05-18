n = 4
A = [
[1, 0, -1],
[0, 2, -1],
[2, 3, -1],
[3, -1, -1]
]

T = [{ 'parent': -1, 'sibling': -1, 'degree': 0, 'depth': 0, 'height': 0 } for _ in range(n)]

for a in A:
  # ノードにid・left・rightを登録
  T[a[0]]['node'] = a[0]
  T[a[0]]['left'] = a[1]
  T[a[0]]['right'] = a[2]

  # ノードに子ノードの数
  # 子ノードにparent
  # 子ノードにsibling
  if a[1] != -1:
    T[a[0]]['degree'] += 1
    T[a[1]]['parent'] = a[0]
    T[a[1]]['sibling'] = a[2]
  if a[2] != -1:
    T[a[0]]['degree'] += 1
    T[a[2]]['parent'] = a[0]
    T[a[2]]['sibling'] = a[1]

def set_height(node_id, height):
  h1 = h2 = height
  if T[node_id]['right'] != -1:
    h1 = set_height(T[node_id]['right'], height + 1)
  if T[node_id]['left'] != -1:
    h2 = set_height(T[node_id]['left'], height + 1)

  return max(h1, h2)


def set_depth(node_id, depth):
  if T[node_id]['parent'] == -1:
    return depth

  return set_depth(T[node_id]['parent'], depth + 1)

for t in T:
  t['depth'] = set_depth(t['node'], 0)
  t['height'] = set_height(t['node'], 0)

  # nodeの種類を登録(root | internal node | leaf)
  if t["depth"] == 0:
    t["type"] = "root"
  elif t["degree"] == 0:
    t["type"] = "leaf"
  else:
    t["type"] = "internal node"

  print(f'node {t["node"]}: parent = {t["parent"]}, sibling = {t["sibling"]}, degree = {t["degree"]}, depth = {t["depth"]}, height = {t["height"]}, {t["type"]}')