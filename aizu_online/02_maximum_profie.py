def main(strings: str) -> int:
  input = [int(i) for i in strings.split(' ')]
  n, r = input[0], input[1:]
  ans = 0
  for i in range(n):
    for j in range(i, n):
      if ans < r[j] - r[i]:
        ans = r[j] - r[i]
  print(ans)


if __name__ == '__main__':
  main("6 5 3 1 3 4 3")