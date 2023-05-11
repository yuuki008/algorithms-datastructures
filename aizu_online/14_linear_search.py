def linear_search(S, T):
  cnt = 0
  for i, i_value in enumerate(T):
    for j, j_value in enumerate(S):
      if i_value == j_value:
        S.pop(j)
        cnt += 1
        break
  print(cnt)

if __name__ == '__main__':
  S = [1, 1, 2, 2, 3]
  T = [1,2]
  linear_search(S, T)