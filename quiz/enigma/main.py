import string
from typing import List
import random

ALPHABET = string.ascii_uppercase

class PlugBoard(object):

  def __init__(self, map_alaphabet):
    self.alphabet = ALPHABET
    self.forward_map = {}
    self.backward_map = {}
    self.mapping(map_alaphabet)

  def mapping(self, map_alaphabet):
    # 'ABCD'
    # 'BADC'
    # { 'A': 'B', 'B': 'A' }
    self.forward_map = dict(zip(self.alphabet, map_alaphabet))
    # { 'B': 'A', 'A': 'B' }
    self.backward_map = { v: k for k, v in self.forward_map.items() }

  def forward(self, index_num):
    char = self.alphabet[index_num]
    char = self.forward_map[char]
    return self.alphabet.index(char)

  def backward(self, index_num):
    char = self.alphabet[index_num]
    char = self.backward_map[char]
    return self.alphabet.index(char)


class Rotor(PlugBoard):
  def __init__(self, map_alphabet, offset=0):
    super().__init__(map_alphabet)
    self.offset = offset
    self.rotations = 0

  def rotate(self, offset=None):
    if not offset:
      offset = self.offset
    self.alphabet = self.alphabet[offset:] + self.alphabet[:offset]
    self.rotations += offset
    return self.rotations

  def reset(self):
    self.rotations = 0
    self.alphabet = ALPHABET

class Reflector(object):
  def __init__(self, map_alpahbet):
    self.map = dict(zip(ALPHABET, map_alpahbet))
    for x, y in self.map.items():
      if x != self.map[y]:
        raise ValueError(x, y)

  def reflect(self, index_num):
    reflected_char = self.map[ALPHABET[index_num]]
    return ALPHABET.index(reflected_char)

class EnigmaMachine(object):
  def __init__(self, plug_board: PlugBoard, rotors: List[Rotor], reflector: Reflector):
    self.plug_board = plug_board
    self.rotors = rotors
    self.refelector = reflector

  def encrypt(self, text):
    return ''.join([self.go_through(c) for c in list(text)])

  def decrypt(self, text):
    for rotor in self.rotors:
      rotor.reset()
    return ''.join([self.go_through(c) for c in list(text)])

  def go_through(self, char):
    char = char.upper()
    if char not in ALPHABET:
      return char

    index_num = ALPHABET.index(char)
    index_num = self.plug_board.forward(index_num)

    for rotor in self.rotors:
      index_num = rotor.forward(index_num)

    index_num = self.refelector.reflect(index_num)

    for rotor in reversed(self.rotors):
      index_num = rotor.backward(index_num)

    index_num = self.plug_board.backward(index_num)
    char = ALPHABET[index_num]

    for rotor in reversed(self.rotors):
      if rotor.rotate() % len(ALPHABET) != 0:
        break

    return char


def get_random_alphabet():
  alphabet = [ALPHABET[i] for i in range(len(ALPHABET))]
  random.shuffle(alphabet)
  return ''.join(alphabet)

if __name__ == '__main__':
  plug_board = PlugBoard(get_random_alphabet())
  rotor01 = Rotor(get_random_alphabet(), 3)
  rotor02 = Rotor(get_random_alphabet(), 2)
  rotor03 = Rotor(get_random_alphabet(), 1)


  r = list(ALPHABET)
  indexes = [i for i in range(len(ALPHABET))]
  for _ in range(int(len(indexes)/2)):
    x = indexes.pop(random.randint(0, len(indexes)-1))
    y = indexes.pop(random.randint(0, len(indexes)-1))
    r[x], r[y] = r[y], r[x]

  refrector = Reflector(r)

  enigma_machine = EnigmaMachine(plug_board, [rotor01, rotor02], refrector)
  text = 'ATTACK SILLICON VALLEY'
  print(text)
  encrypted = enigma_machine.encrypt(text)
  print(encrypted)
  decrypted = enigma_machine.decrypt(encrypted)
  print(decrypted)