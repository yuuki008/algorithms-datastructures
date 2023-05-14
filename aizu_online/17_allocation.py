"""
https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/4/ALDS1_4_D
"""


n = 5
k = 3
w = [8, 1, 7, 3, 9]

def check(p):
  i = 0
  for _ in range(k):
    s = 0
    while s + w[i] <= p:
      s += w[i]
      i += 1
      if len(w) == i:
        return i
  return i

left = 0
right = 10000 * 100000

while right - left > 1:
  p = (left + right) // 2
  if check(p) >= len(w):
    right = p
  else:
    left = p
print(right)
