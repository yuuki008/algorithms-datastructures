# 自分の力で
class Node(object):
  def __init__(self, data) -> None:
    self.data = data
    self.prev = None
    self.next = None

class DoublyLinkedList(object):
  def __init__(self) -> None:
    self.head = None

  def insert(self, x):
    new_node = Node(x)

    if self.head is None:
      self.head = new_node
      return

    temp = self.head
    self.head = new_node
    self.head.next = temp
    temp.prev = new_node

  def delete(self, x):
    current_node = self.head
    if current_node and current_node.data == x:
      if current_node.next is None:
        current_node = None
        self.head = None
      else:
        next_node = current_node.next
        next_node.prev = None
        current_node = None
        self.head = next_node

    while current_node:
      if current_node.data != x:
        current_node = current_node.next
        continue

      if current_node.next is None:
        current_node.prev.next = None
        current_node = None
        return
      else:
        current_node.prev.next = current_node.next
        current_node.next.prev = current_node.prev
        current_node = None
        return

  def deleteFirst(self):
    if self.head is None:
      return
    if self.head.next is None:
      self.head = None
      return

    self.head = self.head.next
    self.head.prev = None

  def deleteLast(self):
    current_node = self.head
    if current_node is None:
      return

    if current_node.next is None:
      self.head = None
      return

    while current_node.next:
      current_node = current_node.next

    current_node.prev.next = None
    current_node = None

  def print_list(self):
    current_node = self.head
    if current_node is None:
      return

    while current_node.next:
      print(current_node.data, end=' ')
      current_node = current_node.next

    print(current_node.data)

def answer():
  from collections import deque
  n = int(input())
  result = deque()
  for loop in range(n):
      command = input()
      if command == 'deleteFirst':
          result.popleft()
      elif command == 'deleteLast':
          result.pop()
      else:
        cmd, x =  command.split()
        if cmd == 'insert':
          result.appendleft(x)
        elif cmd == 'delete':
          try:
            result.remove(x)
          except:
            pass
  print(*result)
if __name__ == '__main__':
  n = 5
  commands = [
    ['insert', 7],
    ['insert', 3],
    ['deleteFirst'],
    ['deleteLast'],
    ['insert', 1],
  ]

  result = DoublyLinkedList()
  for i in range(n):
    if commands[i][0] == 'insert':
      result.insert(commands[i][1])
    elif commands[i][0] == 'delete':
      result.delete(commands[i][1])
    elif commands[i][0] == 'deleteFirst':
      result.deleteFirst()
    elif commands[i][0] == 'deleteLast':
      result.deleteLast()
    else:
      continue

  result.print_list()