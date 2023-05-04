# [1, 3, 3, 5, 5, 7, 7, 7, 10, 12, 12, 15] => [1, 3, 5, 7, 10, 12, 15]
from typing import List

def delete_duplicate_v1(numbers: List[int]):
  tmp = []
  for i in range(len(numbers)):
    if not numbers[i] in tmp:
      tmp.append(numbers[i])
  numbers[:] = tmp

def delete_duplicate_v2(numbers: List[int]):
  tmp = [numbers[0]]
  i, len_num = 0, len(numbers) - 1
  while i < len_num:
    if numbers[i] != numbers[i+1]:
      tmp.append(numbers[i+1])
    i+=1
  numbers[:] = tmp

def delete_duplicate_v3(numbers: List[int]):
  i = 0
  while i < len(numbers) - 1:
    if numbers[i] == numbers[i+1]:
      numbers.pop(i+1)
    else:
      i+=1
  return numbers

def delete_duplicate_v4(numbers: List[int]):
  i = len(numbers) - 1
  while i > 0:
    if numbers[i] == numbers[i-1]:
      numbers.pop(i)
    i -= 1


if __name__ == '__main__':
  numbers = [1, 3, 3, 5, 5, 7, 7, 7, 10, 12, 12, 15]
  delete_duplicate_v4(numbers)
  print(numbers)
