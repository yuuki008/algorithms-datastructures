"""
https://en.wikipedia.org/wiki/Caesar_cipher
https://en.wikipedia.org/wiki/List_of_Unicode_characters
"""
import string
from typing import Generator, Tuple

def caesar_cipher_v1(text: str, shift: int) -> str:
  result = ''
  for char in text:
    if char.isupper():
      alphabet = string.ascii_uppercase
    elif char.islower():
      alphabet = string.ascii_lowercase
    else:
      result += char
      continue
    index = (alphabet.index(char) + shift) % len(alphabet)
    result += alphabet[index]
  return result

def caesar_cipher_v2(text: str, shift: int) -> str:
  result = ''
  len_alphabet = ord('Z') - ord('A') + 1
  for char in text:
    if char.isupper():
      result += chr((ord(char) + shift - ord('A')) % len_alphabet + ord('A'))
    elif char.islower():
      result += chr((ord(char) + shift - ord('a')) % len_alphabet + ord('a'))
    else:
      result += char
  return result

def caesar_cipher_hack_v1(text: str) -> Generator[Tuple[int, str], None, None]:
  len_alphabet = ord('Z') - ord('A') + 1
  for candidate_shift in range(1, len_alphabet + 1):
    reverted = ''
    for char in text:
      if char.isupper():
        alphabet = string.ascii_uppercase
      elif char.islower():
        alphabet = string.ascii_lowercase
      else:
        reverted += char
        continue

      index = alphabet.index(char) - candidate_shift
      if index < 0:
        index += len_alphabet
      reverted += alphabet[index]
    yield candidate_shift, reverted

def caesar_cipher_hack_v2(text: str) -> Generator[Tuple[int, str], None, None]:
  len_alphabet = ord('Z') - ord('A') + 1
  for candidate_shift in range(1, len_alphabet + 1):
    reverted = ''
    for char in text:
      if char.isupper():
        index = ord(char) - candidate_shift
        if index < ord('A'):
          index += len_alphabet
        reverted += chr(index)
      elif char.islower():
        index = ord(char) - candidate_shift
        if index < ord('a'):
          index += len_alphabet
        reverted += chr(index)
      else:
        reverted += char
        continue
    yield candidate_shift, reverted


if __name__ == '__main__':
  text = 'ATTACK SILICON VALLY by engineer'
  e = caesar_cipher_v1(text, 3)
  print(e)
  for shift_num, decrypted in caesar_cipher_hack_v2(e):
    if decrypted == text:
      print(decrypted)