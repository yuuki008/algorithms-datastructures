from typing import List
def main(n: int, r: List[int]) -> List[int]:
  count = 0
  for i in range(n):
    min_value_index = i
    for j in range(i, n):
      if r[min_value_index] > r[j]:
          min_value_index = j
    if i != min_value_index:
      r[i], r[min_value_index] = r[min_value_index], r[i]
      count += 1

if __name__ == '__main__':
  main(6, [6, 5, 4, 3, 2, 1])