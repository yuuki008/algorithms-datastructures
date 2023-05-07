from typing import List

def generate_pascal_triangle_v1(depth: int) -> List[List[int]]:
  items = [[0] * (depth * 2 + 1) for _ in range(depth)]

  items[0][depth] = 1

  for i in range(1, depth):
    for j in range(1, depth * 2):
      items[i][j] = items[i-1][j-1] + items[i-1][j+1]

  return items

def generate_pascal_triangle_v2(depth: int) -> List[List[int]]:
  data = [[1] * (i + 1) for i in range(depth)]

  for line in range(2, depth):
    for i in range(1, line):
      data[line][i] = data[line-1][i-1] + data[line-1][i]
  return data

def print_pascal(data: List[int]) -> None:
  max_digit = len(str(max(data[-1])))
  # (max_digit % 2)は奇数であれば+1で偶数であれば+0している
  width = max_digit + (max_digit  % 2) + 2

  for index, line in enumerate(data):
    numbers  = ''.join([str(i).center(width, ' ') for i in line])
    print((' ' * int(width/2)) * (len(data) - index), numbers)

if __name__ == '__main__':
  for r in generate_pascal_triangle_v1(5):
    print(r)

  data = generate_pascal_triangle_v2(5)
  print_pascal(data)