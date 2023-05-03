from typing import Any
from collections import deque

class Queue(object):
  def __init__(self) -> None:
    self.queue = []

  def enqueue(self, data: Any) -> None:
    self.queue.append(data)

  def dequeue(self) -> Any:
    if self.queue:
      return self.queue.pop(0)


if __name__ == '__main__':
  q = deque()
  q.append(1)
  q.append(2)
  q.append(3)
  q.append(4)
  print(q)
  q.reverse()
  print(q)