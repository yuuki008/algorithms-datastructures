import math

cnt = 0
def merge(A, left, mid, right):
    global cnt
    l_list = A[left:mid] + [math.inf]
    r_list = A[mid:right] + [math.inf]

    i = j = 0
    for k in range(left, right):
        if l_list[i] < r_list[j]:
            A[k] = l_list[i]
            i += 1
        else:
            A[k] = r_list[j]
            cnt += mid - left - i
            j += 1

def merge_sort(A, left, right):
    if right - left > 1:
        mid = (right + left) // 2

        merge_sort(A, left, mid)
        merge_sort(A, mid, right)
        merge(A, left, mid, right)

n = 5
A = [3, 5, 2, 1, 4]
merge_sort(A, 0, n)
print(cnt)