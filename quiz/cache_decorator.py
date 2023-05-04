# Implements decorator to cache func
import time

def memoize(f):
  cache = {}
  def _wrapper(n):
    if n not in cache:
      cache[n] = f(n)
    return cache[n]
  return _wrapper


@memoize
def long_func(num: int) -> int:
  r = 0
  for i in range(10000000):
    r += num * i
  return r

if __name__ == "__main__":
  start = time.time()
  for i in range(10):
    long_func(i)

  first = time.time()
  print('first_time', time.time() - start)
  for i in range(10):
    long_func(i)

  print('second_time', time.time() - first)
  print('full_time', time.time() - start)