""" Generate Prime Numbers
Input: 50 => Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
"""
from typing import List

def generate_primes_v1(number: int) -> List[int]:
  primes = []
  for x in range(2, number + 1):
    for y in range(2, x):
      if x % y == 0:
        break
    else:
      primes.append(x)

  return primes

def generate_primes_v2(number: int) -> List[int]:
  primes = []
  cache = {}
  for x in range(2, number + 1):
    is_prime = cache.get(x)
    if is_prime is False:
      continue
    primes.append(x)
    cache[x] = True
    for y in range(x*2, number+1, x):
      cache[y] = False
  return primes


if __name__ == '__main__':
  print(generate_primes_v1(50))
