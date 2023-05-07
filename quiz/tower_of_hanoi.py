from typing import List, Tuple
# A, B, C
def hanoi(disk: int, start: str, dest: str, supoort: str):
  if disk < 1:
    return

  hanoi(disk-1, start, supoort, dest)
  print(f'move {disk} from {start} to {dest}')
  hanoi(disk-1, supoort, dest, start)


def get_hanoi_movement(disk: int, src: str, dest: str, support: str) -> List[Tuple[int, str, str]]:
  result = []

  def _hanoi(disk: int, start: str, dest: str, supoort: str):
    if disk < 1:
      return

    _hanoi(disk-1, start, supoort, dest)
    result.append((disk, src, dest))
    _hanoi(disk-1, supoort, dest, start)
  _hanoi(disk, src, dest, support)
  return result

if __name__ == '__main__':
  for r in get_hanoi_movement(4, 'A', 'C', 'B'):
    print(r)

"""
move 1 from A to C
move 2 from A to B
move 1 from C to B
move 3 from A to C
move 1 from B to A
move 2 from B to C
move 1 from A to C
"""