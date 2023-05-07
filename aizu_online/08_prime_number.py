from typing import List
import math

def main(n: int, nums: List[int]) -> int:
  ans = 0
  for i in range(n):
    for j in range(2, int(math.sqrt(nums[i])) - 1):
      if nums[i] % j == 0:
        break
    else:
      ans += 1

  print(ans)
if __name__ == "__main__":
  main(16, [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1])