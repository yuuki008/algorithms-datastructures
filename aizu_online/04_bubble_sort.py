from typing import List
def main(n: int, r: List[int]) -> List[int]:
  count = 0
  for i in range(len(r)):
    for j in range(len(r) - 1 - i):
      if r[j] > r[j+1]:
        count += 1
        r[j], r[j+1] = r[j+1], r[j]
  print(r)
  print(count)

if __name__ == '__main__':
  main(20, [0, 33, 43, 62, 29, 0, 8, 52, 56, 56, 19, 11, 51, 43, 5, 8, 93, 30, 66, 69])