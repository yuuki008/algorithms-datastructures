def insertion_sort(A, n, g):
  global cnt
  for i in range(g, n):
    v = A[i]
    j = i - g
    while j >= 0 and A[j] > v:
      A[j+g] = A[j]
      j = j - g
      cnt += 1
    A[j+g] = v
    return cnt

def shell_sort(n, A):
  global cnt
  cnt = 0
  g = []
  h = 1
  while h <= len(A):
    g.append(h)
    h = 3*h + 1
  g.reverse()
  m = len(g)
  print(m)
  print(' '.join(map(str, g)))
  for i in range(m):
    insertion_sort(A, n, g[i])
  print(cnt)
  for num in A: print(num)



if __name__ == '__main__':
  n = 5
  g = [5, 1, 4, 3, 2]
  shell_sort(n, g)