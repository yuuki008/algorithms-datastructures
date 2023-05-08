"""
https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/3/ALDS1_3_A
"""

def calculate_reverse_polish_notation(chars: str):
  stack = []
  for char in chars:
    if char.isdigit():
      stack.append(char)
    else:
      stack[-1] = eval(f'{stack[-2]} {char} {stack.pop(-1)}')
  print(stack[0])


if __name__ == '__main__':
  s = '34 116 + 20 5 - 5 - 1 * +'
  chars = s.split(' ')
  calculate_reverse_polish_notation(chars)