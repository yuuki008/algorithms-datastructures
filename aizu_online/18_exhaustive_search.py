# n <= 20
# q <= 200
# 1 <= A[i] <= 2000
# 1 <= M[i] <= 2000

n = 5
q = 10
A = [1, 5, 7, 10, 21]
M = [2, 4, 6, 15, 17, 8, 22, 21, 100, 35]

# Mの最大範囲である2000個の配列を作り、Aの全て組み合わせの合計値を出す
# M[Aの組み合わせの合計値]にTrueを配置
# 最大計算量 = 2 ** 20
m_MAX = 2000
table = [False] * (m_MAX+1)
def solve2(i, m):
  if m > m_MAX:
    return
  if i == n:
    table[m] = True
    return
  solve2(i+1, m)
  solve2(i+1, m+A[i])
solve2(0, 0)

for i in range(q):
  if table[M[i]]:
    print('yes')
  else:
    print('no')


# python3やと計算料オーバーする(Cだといけるっぽい)
# 最大計算量 = 2 ** 20 * 200
# def solve(i, m):
#   if m == 0:
#     return True
#   elif i >= n:
#     return False
#   return solve(i+1, m) or solve(i+1, m - A[i])

# for i in range(q):
#   if solve(0, M[i]):
#     print('yes')
#   else:
#     print('no')