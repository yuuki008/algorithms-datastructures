# [0, 1, 3, 4, 2, 4, 5, 1, 6, 9, 8] => [0, 4, 2, 4, 6, 8, 1, 3, 5, 1, 9]

from typing import List

def order_even_first_odd_last_v1(numbers: List[int]) -> None:
  even_list = []
  odd_list = []
  for num in numbers:
    if num % 2 == 0:
      even_list.append(num)
    else:
      odd_list.append(num)
  numbers[:] = even_list + odd_list

def order_even_first_odd_last_v2(numbers: List[int]) -> None:
  even_index = 0
  for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
      numbers[even_index], numbers[i] = numbers[i], numbers[even_index]
      even_index += 1

def order_even_first_odd_last_v3(numbers: List[int]) -> None:
  i,j = 0, len(numbers) - 1
  while i < j:
    if numbers[i] % 2 == 1:
      numbers[i], numbers[j] = numbers[j], numbers[i]
      j -= 1
    else:
      i += 1

if __name__ == '__main__':
  numbers = [0, 1, 3, 4, 2, 4, 5, 1, 6, 9, 8]
  # order_even_first_odd_last_v1(numbers)
  # order_even_first_odd_last_v2(numbers)
  order_even_first_odd_last_v3(numbers)
  print(numbers)