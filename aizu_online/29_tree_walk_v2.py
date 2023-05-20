import sys
write= sys.stdout.write

n = 4
A = [
[1, 0 ,-1],
[0, 2 ,-1],
[2, 3 ,-1],
[3, -1, -1],
]

L, R, P = [None] * n, [None] * n, [-1] * (n + 1)
for i in range(n):
  i, l, r = A[i]
  L[i] = l
  R[i] = r
  P[l] = i
  P[r] = i

pre_order_list = []; in_order_list = []; post_order_list = []
def dfs(v):
  v0 = str(v)
  pre_order_list.append(v0)
  L[v] != -1 and dfs(L[v])
  in_order_list.append(v0)
  R[v] != -1 and dfs(R[v])
  post_order_list.append(v0)

# Pが-1なのはルートノード
dfs(P.index(-1))
write("Preorder\n %s\nInorder\n %s\nPostorder\n %s\n" % tuple(map(" ".join, [pre_order_list, in_order_list, post_order_list])))
