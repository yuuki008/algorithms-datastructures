n = 10
A = [None, 4, 1, 3, 2, 16, 9, 10, 14, 8, 7]

def max_heapify(A, i):
    l = i * 2
    r = i * 2 + 1
    largest = i
    if l <= n and A[l] > A[i]:
        largest = l
    if r <= n and A[r] > A[largest]:
        largest = r

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest)

for i in range(n//2, 0, -1):
    max_heapify(A, i)
print("", *A[1:])