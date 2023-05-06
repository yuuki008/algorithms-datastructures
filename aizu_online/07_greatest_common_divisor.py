from typing import List

def main(x: int, y:int ) -> int:
  mod = x % y
  if mod == 0:
    return y

  return main(y, mod)


if __name__ == '__main__':
  print(main(147, 105))