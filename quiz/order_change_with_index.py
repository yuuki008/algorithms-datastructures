"""
Input : ['h', 'y', 'n', 'p', 't', 'o'], [3, 1, 5, 0, 2, 4]
Output: python
"""
from typing import List

def order_change_with_index_v1(strings: List[str], numbers: List[int]) -> str:
  result = ['' for _ in range(len(strings))]
  for i in range(len(strings)):
    result[numbers[i]] = strings[i]
  return ''.join(result)

def order_change_with_index_v2(strings: List[str], numbers: List[int]) -> str:
  for i in range(len(strings)):
    strings[numbers[i]], strings[i] = strings[i], strings[numbers[i]]
    numbers[numbers[i]], numbers[i] = numbers[i], numbers[numbers[i]]
  return ''.join(strings)

def order_change_with_index_v3(chars: List[str], indexes: List[int]) -> str:
  i, len_indexes = 0, len(indexes) - 1
  while i < len_indexes:
    while i != indexes[i]:
      index = indexes[i]
      chars[index], chars[i] = chars[i], chars[index]
      indexes[index], indexes[i] = indexes[i], indexes[index]
    i+= 1
  return ''.join(chars)

if __name__ == '__main__':
  strings = ['h', 'y', 'n', 'p', 't', 'o']
  numbers = [3, 1, 5, 0, 2, 4]
  # print(order_change_with_index_v1(strings, numbers))
  # print(order_change_with_index_v2(strings, numbers))
  print(order_change_with_index_v3(strings, numbers))

