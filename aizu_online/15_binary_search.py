S = [1, 2, 3, 4, 5]
T = [3, 4, 1]

cnt = 0
for i in range(len(T)):
  left = 0
  right = len(S)
  while left < right:
    mid = (left + right) // 2
    if S[mid] == T[i]:
      cnt += 1
      break
    elif S[mid] > T[i]:
      right = mid
    else:
      left = mid + 1
print(cnt)
