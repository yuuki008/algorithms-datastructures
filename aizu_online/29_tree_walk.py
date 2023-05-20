n = 4
A = [
[1, 0 ,-1],
[0, 2 ,-1],
[2, 3 ,-1],
[3, -1, -1],
]
d = [{} for _ in range(n)]
for i in range(len(A)):
  d[A[i][0]]['node'] = A[i][0]
  d[A[i][0]]['left'] = A[i][1]
  d[A[i][0]]['right'] = A[i][2]
  d[A[i][1]]['parent'] = A[i][0]
  d[A[i][2]]['parent'] = A[i][0]

def get_max_height_node(A):
  def _height(node, height):
    if node == -1:
      return height

    left_height = _height(d[node]['left'], height + 1)
    right_height = _height(d[node]['right'], height + 1)
    return max(left_height, right_height)
  max_height = 0
  max_height_node = A[0]
  for a in A:
    print(_height(a[0],0))
    current_node_height = _height(a[0], 0)
    if current_node_height > max_height:
      max_height = current_node_height
      max_height_node = a
  return max_height_node[0]

pre_order_list = []
def pre_order(node):
  def _pre_order(a):
    if a == -1:
      return

    pre_order_list.append(a)
    _pre_order(d[a]['left'])
    _pre_order(d[a]['right'])
  _pre_order(d[node]['node'])

in_order_list = []
def in_order(node):
  def _in_order(a):
    if a == -1:
      return

    _in_order(d[a]['left'])
    in_order_list.append(a)
    _in_order(d[a]['right'])
  _in_order(d[node]['node'])

post_order_list = []
def post_order(node):
  def _post_order(a):
    if a == -1:
      return

    _post_order(d[a]['left'])
    _post_order(d[a]['right'])
    post_order_list.append(a)
  _post_order(d[node]['node'])

max_depth_node = get_max_height_node(A)
pre_order(max_depth_node)
in_order(max_depth_node)
post_order(max_depth_node)

print('Preorder')
print(''.join(' ' + str(num) for num in pre_order_list))

print('Inorder')
print(''.join(' ' + str(num) for num in in_order_list))

print('Postorder')
print(''.join(' ' + str(num) for num in post_order_list))