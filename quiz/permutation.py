from typing import List

def all_perms_v1(elements: List[int]) -> List[List[int]]:
  result = []
  if len(elements) <= 1:
    return [elements]
  else:
    for perm in all_perms_v1(elements[1:]):
      print('perm     = ', perm)
      print('elements = ', elements)
      for i in range(len(elements)):
        print(perm[:i], elements[0:1], perm[i:])
        result.append(perm[:i] + elements[0:1] + perm[i:])
      print('result   = ', result)
  return result


if __name__ == '__main__':
  elements = [1, 2, 3]
  for p in all_perms_v1(elements):
    print(p)