from typing import List

def show(c):
  for i in range(len(c)):
    if i == len(c) - 1:
      print(c[i])
    else:
      print(c[i], end=' ')

def show_is_stable(unsorted: List[int], sorted: List[int]):
  is_stable = True
  for i in range(len(sorted) - 1):
    if sorted[i][1] == sorted[i+1][1] and unsorted.index(sorted[i]) > unsorted.index(sorted[i+1]):
      is_stable = False

  if is_stable:
    print('Stable')
  else:
    print('Not stable')

def bubble_sort(c, n):
    numbers = c[:]
    for i in range(1, n):
        temp = numbers[i]
        j = i - 1
        while j >= 0 and int(numbers[j][1]) > int(temp[1]):
            numbers[j+1] = numbers[j]
            j -= 1
        numbers[j+1] = temp
    return numbers

def selection_sort(c, n):
    numbers = c[:]
    for i in range(n):
        min_idx = i
        for j in range(i, len(numbers)):
            if numbers[j][1] < numbers[min_idx][1]:
                min_idx = j
        if i != min_idx:
            numbers[min_idx], numbers[i] = numbers[i], numbers[min_idx]
    return numbers

def main(n, c: List[int]):
  b_nums = bubble_sort(c, n)
  show(b_nums)
  show_is_stable(c, b_nums)

  s_nums = selection_sort(c, n)
  show(s_nums)
  show_is_stable(c, s_nums)

if __name__ == '__main__':
  main(5, ['H4', 'C9', 'S4','D2', 'C3'])