import math

# これだと計算量オーバー
# cnt = 0
# def merge_sort(data: list, l: int, m: int, r: int) -> list:
#     len_left, len_right = m - l + 1, r - m
#     left, right = [], []
#     for i in range(0, len_left):
#         left.append(data[l + i])
#     for i in range(0, len_right):
#         right.append(data[m + 1 + i])

#     i, j, k = 0, 0, l
#     while i < len_left and j < len_right:
#         if left[i] <= right[j]:
#             data[k] = left[i]
#             i += 1
#         else:
#             data[k] = right[j]
#             j += 1
#         k += 1

#     while i < len_left:
#         data[k] = left[i]
#         k += 1
#         i += 1

#     while j < len_right:
#         data[k] = right[j]
#         k += 1
#         j += 1

#     return data

def merge(a_list, left, mid, right):
  l_list = a_list[left:mid] + [math.inf]
  r_list = a_list[mid:right] + [math.inf]

  i = 0
  j = 0
  for k in range(left, right):
    if l_list[i] < r_list[j]:
      a_list[k] = l_list[i]
      i += 1
    else:
      a_list[k] = r_list[j]
      j += 1
  return right - left

def merge_sort(a_list, left, right):
  if left + 1 < right:
    mid = (left + right) // 2
    left_cnt = merge_sort(a_list, left, mid)
    right_cnt = merge_sort(a_list, mid, right)
    return merge(a_list, left, mid, right) + left_cnt + right_cnt
  return 0
n = 10
S = [8, 5, 9, 2, 6, 3, 7, 1, 10, 4]

cnt = merge_sort(S, 0, len(S))
print(*S)
print(cnt)

