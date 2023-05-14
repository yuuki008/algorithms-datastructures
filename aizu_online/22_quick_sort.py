def is_stable(unsorted, sorted):
    for i in range(len(sorted)-1):
        if sorted[i][1] == sorted[i+1][1] and unsorted.index(sorted[i]) > unsorted.index(sorted[i+1]):
            return 'Not stable'
    return 'Stable'

def partition(A, p, r):
  pivot = A[r][1]
  i = p - 1
  for j in range(p, r):
    if A[j][1] <= pivot:
      i += 1
      A[i], A[j] = A[j], A[i]
  A[i+1], A[r] = A[r], A[i+1]
  return i + 1

def quick_sort(A, p, r):
  if p < r:
    q = partition(A, p, r)
    quick_sort(A, p, q-1)
    quick_sort(A, q+1, r)

n = 6
A = [("D", 3), ("H", 2), ("D", 1), ("S", 3), ("D", 2), ("C", 1)]
# n = int(input())
# A = []
for _ in range(n):
    a, b = input().split()
    A.append((a, int(b)))
unsorted = A[:]
quick_sort(A, 0, len(A) - 1)
print(is_stable(unsorted, A))
for i in range(len(A)):
    print(A[i][0], A[i][1])
