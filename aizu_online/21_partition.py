def partition(A, p, r):
    temp = A[r]
    i = p - 1
    for j in range(p, r):
      if A[j] <= temp:
        i = i + 1
        A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = f'[{A[r]}]', A[i+1]
    return i+1



n = 12
A = [13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11]
partition(A, 0, len(A)-1)
print(*A)