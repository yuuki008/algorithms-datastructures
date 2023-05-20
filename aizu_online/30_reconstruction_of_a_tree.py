n = 5
pre_order = [1, 2, 3, 4, 5]
in_order = [3, 2, 4, 1, 5]
# n = int(input())
# pre_order = list(map(int, input().split()))
# in_order = list(map(int, input().split()))
tree = [None] * (n + 1)

def recontruct(pre_tree, in_tree):
    if not pre_tree:
        return -1

    root = pre_tree[0]
    i = in_tree.index(root)
    tree[root] = (recontruct(pre_tree[1:i+1], in_tree[:i]), recontruct(pre_tree[i+1:], in_tree[i+1:]))
    return root

post_order_list = []
def post_order(i):
    if i == -1:
        return
    l,r = tree[i]
    post_order(l)
    post_order(r)
    post_order_list.append(i)
recontruct(pre_order, in_order)
post_order(pre_order[0])
print(*post_order_list)