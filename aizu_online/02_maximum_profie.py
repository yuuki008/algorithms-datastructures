def main(strings: str) -> int:
  input = [int(i) for i in strings.split(' ')]
  n, r = input[0], input[1:]
  ans = -1e10
  for i in range(len(r)):
    for j in range(i + 1, len(r)):
      ans = max(ans, r[j] - r[i])
  print(ans)

def main_v2(strings: str) -> int:
  input = [int(i) for i in strings.split(' ')]
  n, r = input[0], input[1:]
  print(n, r)
  min_value = r[0]
  max_value = -1e10
  for i in range(1, len(r)):
    max_value = max(max_value, r[i] - min_value)
    min_value = min(r[i], min_value)
  print(max_value)


if __name__ == '__main__':
  main_v2('20 100 99 95 86 85 76 75 71 70 61 52 48 47')