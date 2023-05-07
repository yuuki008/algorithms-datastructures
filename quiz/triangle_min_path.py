"""
Input 5, 20
Output
[[7], [6, 3], [6, 0, 15], [4, 20, 1, 8], [6, 4, 4, 1, 0]]
            7
          6   3
        6   0   15
      4   20  1   8
    6   4   4   1   0
min path = 12
"""
from typing import List
import random

def generate_triangle_list(depth: int, max_num: int) -> List[List[int]]:
  return [[random.randint(0, max_num) for _ in range(i)] for i in range(1, depth + 1)]

def print_trianble(data: List[List[int]]) -> None:
  max_digit = len(str(max([max(l) for l in data])))
  width = max_digit + (max_digit % 2) + 2
  for index, line in enumerate(data):
    numbers = ''.join(str(i).center(width, ' ') for i in line)
    print(' ' * int(width / 2) * (len(data) - index), numbers)

def sum_min_path_v1(triangle_list: List[List[int]]) -> List[List[int]]:
  current_depth = 0
  current_index = 0
  min_path = triangle_list[0][0]
  while current_depth < len(triangle_list) - 1:
    left = triangle_list[current_depth+1][current_index]
    right = triangle_list[current_depth+1][current_index+1]
    if right < left:
      min_path += right
      current_index += 1
    else:
      min_path += left
    current_depth += 1

  print(min_path)


if __name__ == '__main__':
  triangle_list = generate_triangle_list(5, 20)
  print_trianble(triangle_list)
  sum_min_path_v1(triangle_list)