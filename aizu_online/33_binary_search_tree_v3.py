class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

def insert(node, root):
    current = root
    parent = None
    while current:
        parent = current
        if node.value < current.value:
            current = current.left
        else:
            current = current.right

    node.parent = parent
    if parent is None:
        return node
    elif node.value < parent.value:
        parent.left = node
    else:
        parent.right = node
    return root

def find(value, root):
    current = root
    while current:
        if value == current.value:
            print('yes')
            return
        elif value < current.value:
            current = current.left
        else:
            current = current.right
    print('no')

def min_value(node):
    current = node
    while current.left:
        current = current.left
    return current

def delete(value, node):
    if node is None:
        return node

    if value < node.value:
        node.left = delete(value, node.left)
    elif value > node.value:
        node.right = delete(value, node.right)
    else:
        if node.left is None:
            return node.right
        if node.right is None:
            return node.left

        temp = min_value(node.right)
        node.value = temp.value
        node.right = delete(temp.value, node.right)
    return node

def print_in_order(node):
    if node is None:
        return node


    print_in_order(node.left)
    print(f' {node.value}', end='')
    print_in_order(node.right)
    return

def print_pre_order(node):
    if node is None:
        return node

    print(f' {node.value}', end='')
    print_pre_order(node.left)
    print_pre_order(node.right)
    return


n = int(input())
root = None
for _ in range(n):
    line = list(input().split())
    if line[0] == 'insert':
        node = Node(int(line[1]))
        root = insert(node, root)
    elif line[0] == 'find':
        find(int(line[1]), root)
    elif line[0] == 'delete':
        delete(int(line[1]), root)
    else:
        print_in_order(root)
        print()
        print_pre_order(root)
        print()