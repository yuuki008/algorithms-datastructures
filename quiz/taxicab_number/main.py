# https://en.wikipedia.org/wiki/Taxicab_number
# 1729 = Ta(2) = 1**3 + 12**3 = 9**3 + 10**3
# Input 1, 2 => [(1729, [(1, 12), (9, 10)])]
# Input 2, 2 => [(1729, [(1, 12), (9, 10)]), (4104, [(2, 16), (9, 15)])]
# Input 1, 3 => [(87539319, [(167, 436), (228, 423), (255, 414)])]
from collections import defaultdict
from typing import List, Tuple

def taxi_cab_number_v1(max_answer_num: int, match_answer_num: int=2) -> List[Tuple[int, List[Tuple[int, int]]]]:
  print(max_answer_num, match_answer_num)
  numbers = {}
  for i in range(1, 100):
    for j in range(1, 100):
      if i ** 3 + j ** 3 == 1729:
        numbers[i**3 + j**3] = numbers.get(i ** 3 + j ** 3, 0) + 1

  result = []
  for key, value in numbers.items():
    if value == match_answer_num * 2:
      result.append(key)
    if len(result) >= max_answer_num:
      break
  return result

def taxi_cab_number_v2(max_answer_num: int, match_answer_num: int=2, start_answer: int = 1) -> List[Tuple[int, List[Tuple[int, int]]]]:
  result = []
  got_answer_count = 0
  answer = start_answer
  while got_answer_count < max_answer_num:
    match_answer_count = 0
    memo = defaultdict(list)

    max_param = int(pow(answer, 1 / 3)) + 1
    for x in range(1, max_param):
      for y in range(x+1, max_param):
        if x ** 3 + y ** 3 == answer:
          match_answer_count += 1
          memo[answer].append((x, y))

    if match_answer_count == match_answer_num:
      result.append((answer, memo[answer]))
      got_answer_count += 1

    answer += 1
  return result


if __name__ == '__main__':
  # print(taxi_cab_number_v1(1,2))
  print(taxi_cab_number_v2(1,3,87539319))
