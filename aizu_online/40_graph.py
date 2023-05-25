n = int(input())
A = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(n):
    a = list(map(int, input().split()))
    temp = a[0]
    for num in a[2:]:
        A[temp][num] = 1

for i in range(1, n+1):
    print(*A[i][1:])