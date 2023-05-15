
def counting_sort(A, B, k):
  C = [0 for _ in range(k)]

  for j in range(n):
    C[A[j]] += 1

  for i in range(k):
    C[i] += C[i-1]

  i = len(A) - 1
  while i >= 0:
    B[C[A[i]]] = A[i]
    C[A[i]] -= 1
    i -= 1
  print(B)


k = 10001
n = 7
A = [2, 5, 1, 3, 2, 3, 0]
B = [0 for _ in range(n+1)]
counting_sort(A, B, k)

