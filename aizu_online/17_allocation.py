def check(w, p, k):
    i = 0
    for _ in range(k):
        s = 0
        while s + w[i] <= p:
            s += w[i]
            i += 1
            if i == len(w):
                return len(w)
    return i

n, k = map(int, input().split())
w = [int(input()) for _ in range(n)]

right = 100000 * 10000
left = 0
while right - left > 1:
    p = (right + left) // 2
    if check(w, p, k) >= len(w):
        right = p
    else:
        left = p
print(right)




n = 5
k = 3
w = [8, 1, 7, 3, 9]
allocation(w, k)