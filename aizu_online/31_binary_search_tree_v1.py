import sys

# READ_FROM_FILE = True
READ_FROM_FILE = False


class Node:
    def __init__(self, parent, key):
        self.key = key
        self.parent = parent
        self.left = None
        self.right = None
        return


def insert(root, i_n):
    parent = None
    c_n = root

    while c_n is not None:
        parent = c_n

        if i_n.key < c_n.key:
            c_n = c_n.left
        else:
            c_n = c_n.right

    i_n.parent = parent
    if root is None:
        root = i_n
    elif i_n.key < parent.key:
        parent.left = i_n
    else:
        parent.right = i_n

    return root


def print_in_order(c_n):
    if c_n is None:
        return

    print_in_order(c_n.left)
    print(f' {c_n.key}', end='')
    print_in_order(c_n.right)
    return


def print_pre_order(c_n):
    if c_n is None:
        return

    print(f' {c_n.key}', end='')
    print_pre_order(c_n.left)
    print_pre_order(c_n.right)
    return


def main():
    if READ_FROM_FILE:
        f = open('test0.txt', 'r')
    else:
        f = sys.stdin

    m = int(f.readline())
    root = None

    for _ in range(m):
        op = f.readline().split()

        if len(op) > 1:
            key = int(op[1])
            node = Node(None, key)
            root = insert(root, node)
        else:
            print_in_order(root)
            print()
            print_pre_order(root)
            print()

    if READ_FROM_FILE:
        f.close()
    return


if __name__ == '__main__':
    main()

