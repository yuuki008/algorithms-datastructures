"""
input [25, 36, 4, 55, 71, 18, 0, 71, 89, 65]
output [89, 71, 71]
"""
from typing import List

def get_top_n_v1(numbers: List[int], n) -> List[int]:
  for i in range(n):
    j = len(numbers) - 1
    while j > i:
      if numbers[j] > numbers[j-1]:
        numbers[j-1], numbers[j] = numbers[j], numbers[j-1]
      j -= 1
  return numbers[:n]

def get_top_n_v2(numbers: List[int], n) -> List[int]:
  result = []
  for _ in range(n):
    max_num = max(numbers)
    result.append(max_num)
    numbers.remove(max_num)
  return result

def get_top_n_v3(numbers: List[int], n) -> List[int]:
  all_points = [0] * 100

  for i in range(len(numbers)):
    all_points[numbers[i]] += 1

  result = []
  index = len(all_points) - 1
  while len(result) < n and index > 0:
    [result.append(index) for _ in range(all_points[index])]
    index -= 1
  return result



if __name__ == '__main__':
  numbers = [25, 36, 4, 55, 71, 18, 0, 71, 89, 65]
  # print(get_top_n_v1(numbers, 3))
  # print(get_top_n_v2(numbers, 3))
  print(get_top_n_v3(numbers, 4))
