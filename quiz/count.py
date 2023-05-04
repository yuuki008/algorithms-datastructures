# Input: 'This is a pen. This is an apple. Applepen.'
# Output: ('p', 6)
from collections import Counter
import operator
from typing import Tuple

def count_chars_v1(strings: str) -> Tuple[str, int]:
  strings = strings.lower()
  l = []
  for char in strings:
    if not char.isspace():
      l.append((char, strings.count(char)))

  return max(l, key=operator.itemgetter(1))


def count_chars_v2(strings: str) -> Tuple[str, int]:
  cache = {}
  strings = strings.lower()
  for char in strings:
    if not char.isspace():
      cache[char] = cache.get(char, 0) + 1
  max_key = max(cache, key=cache.get)
  return max_key, cache[max_key]

def count_chars_v3(strings: str) -> Tuple[str, int]:
  strings = strings.lower()
  d = Counter()
  for char in strings:
    if not char.isspace():
      d[char] += 1
  max_key = max(d, key=d.get)
  return max_key, d[max_key]

if __name__ == "__main__":
  s = 'This is a pen. This is an apple. Applepen'
  print(count_chars_v1(s))
  print(count_chars_v2(s))
  print(count_chars_v3(s))
