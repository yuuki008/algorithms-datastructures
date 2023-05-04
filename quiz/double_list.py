"""
Input  X: [1, 2, 3, 4, 4, 5, 5, 8, 10] Y: [4, 5, 5, 5, 6, 7, 8, 8, 10]
Output X: [1, 2, 3, 4, 4, 10]          Y: [5, 5, 5, 6, 7, 8, 8, 10]
"""

from typing import List
from collections import Counter

def double_list(x: List[int], y: List[int]) -> None:
  counter_x = Counter(x)
  counter_y = Counter(y)


  for key_x, value_x in counter_x.items():
    value_y = counter_y.get(key_x)
    if value_y:
      if value_x < value_y:
        x[:] = [i for i in x if i != key_x]
      elif value_x > value_y:
        y[:] = [i for i in y if i != key_x]



if __name__ == "__main__":
  x = [1, 2, 3, 4, 4, 5, 5, 8, 10]
  y = [4, 5, 5, 5, 6, 7, 8, 8, 10]
  print('x = ', x)
  print('y = ', y)
  double_list(x, y)
  print('x = ', x)
  print('y = ', y)