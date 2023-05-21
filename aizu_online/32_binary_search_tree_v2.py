class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
    self.parent = None


def insert(node: Node, root: Node):
    parent_node = None
    current_node = root

    while current_node is not None:
        parent_node = current_node

        if node.value < current_node.value:
            current_node = current_node.left
        else:
            current_node = current_node.right

    node.parent = parent_node
    if root is None:
        root = node
    elif node.value < parent_node.value:
        parent_node.left = node
    else:
        parent_node.right = node

    return root

def find(value, root):
  current_node = root
  while current_node:
    if current_node.value == value:
      print('yes')
      return
    elif value < current_node.value:
      current_node = current_node.left
    else:
      current_node = current_node.right
  print('no')

def print_in_order(node: Node):
    if node is None:
        return

    print_in_order(node.left)
    print(f' {node.value}', end='')
    print_in_order(node.right)
    return


def print_pre_order(node: Node):
    if node is None:
        return

    print(f' {node.value}', end='')
    print_pre_order(node.left)
    print_pre_order(node.right)
    return

n = 24
orders = [
['insert', 8],
['insert', 2],
['insert', 3],
['insert', 7],
['insert', 22],
['insert', 1],
['insert', 10],
['insert', 9],
['insert', 15],
['insert', 13],
['find', 8],
['find', 2],
['find', 3],
['find', 7],
['find', 22],
['find', 1],
['find', 10],
['find', 9],
['find', 15],
['find', 13],
['find', 4],
['find', 5],
['find', 100],
['print']
]

root = None
for i in range(n):
  if orders[i][0] == 'insert':
    node = Node(int(orders[i][1]))
    root = insert(node, root)
  elif orders[i][0] == 'find':
    find(int(orders[i][1]), root)
  else:
    print_in_order(root)
    print()
    print_pre_order(root)
    print()