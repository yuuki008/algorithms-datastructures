from typing import List

def show (nums):
    for i in range(len(nums)):
        if i !=len(nums)-1:
            print(nums[i], end=' ')
        else :
            print(nums[i])

def insertion_sort(n: int, r: List[int]):
  show(r)
  for i in range(1, n):
      temp = r[i]
      j = i - 1
      while j >= 0 and r[j] > temp:
          r[j+1] = r[j]
          j -= 1
      r[j+1] = temp
      show(r)

if __name__ == "__main__":
  insertion_sort(6, [5, 2, 4, 6, 1, 3])
