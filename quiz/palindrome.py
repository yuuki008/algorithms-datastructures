"""
1. Check palindrome
aba => True
abe => False
rececar => True

2. Find palidrome
abcracecarbda => cec, aceca, racecar
"""


def find_palidrome(strings, left: int, right: int):
  result = []
  while 0 <= left and right <= len(strings) - 1:
    if strings[left] != strings[right]:
      break
    result.append(strings[left: right+1])
    left -= 1
    right += 1
  return result

def find_all_palindrome(strings: str):
  result = []
  len_strings = len(strings)
  if not len_strings:
    return result
  if len_strings == 1:
    result.append(1)

  for i in range(1, len_strings-1):
    [result.append(s) for s in find_palidrome(strings, i-1, i+1)]
    [result.append(s) for s in find_palidrome(strings, i-1, i)]

  return result



def is_palindrome(strings: str) -> bool:
  len_string = len(strings)

  if not len_string:
    return False
  if len_string == 1:
    return True

  start, end = 0, len_string - 1

  while start < end:
    if strings[start] != strings[end]:
      return False
    start += 1
    end -= 1
  return True

if __name__ == '__main__':
  s = 'racecar'
  # print(s == ''.join(reversed(s)))
  # print(s == s[::-1])
  # print(is_palindrome(s))
  print(find_all_palindrome('abcracecarbda'))