n = 9
A = [
[3, 4, 0],
[4, -1, -1],
[1, -1, -1],
[2, -1, -1],
[0, 1, 2]
]
d = [{} for _ in range(n)]
for i in range(len(A)):
  d[A[i][0]]['node'] = A[i][0]
  d[A[i][0]]['left'] = A[i][1]
  d[A[i][0]]['right'] = A[i][2]

pre_order_list = []
def pre_order(A):
  def _pre_order(a):
    if a == -1:
      return

    pre_order_list.append(a)
    _pre_order(d[a]['left'])
    _pre_order(d[a]['right'])
  _pre_order(d[A[0][0]]['node'])

in_order_list = []
def in_order(A):
  def _in_order(a):
    if a == -1:
      return

    _in_order(d[a]['left'])
    in_order_list.append(a)
    _in_order(d[a]['right'])
  _in_order(d[A[0][0]]['node'])

post_order_list = []
def post_order(A):
  def _post_order(a):
    if a == -1:
      return

    _post_order(d[a]['left'])
    _post_order(d[a]['right'])
    post_order_list.append(a)
  _post_order(d[A[0][0]]['node'])

pre_order(A)
in_order(A)
post_order(A)

print('Preorder')
print(' ', *pre_order_list, ' ')
print(''.join(' ' + str(num) for num in pre_order_list))

print('Inorder')
print(' ', *in_order_list, ' ')

print('Postorder')
print(' ', *post_order_list, ' ')