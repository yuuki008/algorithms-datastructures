"""
Input 568-379-8466 Output [..., 'LOVEPYTHON', ... ]
Input 435-569-6753 Output [..., 'HELLOWORLD', ...]
"""
from typing import List, NewType

NUM_ALPHABET_MAPPING = {
  0: '+',
  1: '@',
  2: 'ABC',
  3: 'DEF',
  4: 'GHI',
  5: 'JKL',
  6: 'MNO',
  7: 'PQRS',
  8: 'TUV',
  9: 'WXYZ'
}

def phone_mnemonic_v1(phone_number: str) -> List[str]:
    phone_number = [int(s) for s in phone_number.replace('-', '')]
    candidate = []
    tmp= [''] * len(phone_number)

    def find_candidate_alphabet(digit: int = 0) -> None:
        if digit == len(phone_number):
            candidate.append(''.join(tmp))
        else:
            for char in NUM_ALPHABET_MAPPING[phone_number[digit]]:
                tmp[digit] = char
                find_candidate_alphabet(digit+1)

    find_candidate_alphabet()
    return candidate

def phone_mnemonic_v2(phone_number: str) -> List[str]:
  phone_number = [int(s) for s in phone_number.replace('-', '')]
  candidate = []
  stack = ['']

  while len(stack) != 0:
    alphabets = stack.pop()
    if len(alphabets) == len(phone_number):
      candidate.append(alphabets)
    else:
      for char in NUM_ALPHABET_MAPPING[phone_number[len(alphabets)]]:
        stack.append(alphabets + char)
  return candidate


if __name__ == '__main__':
  for i in phone_mnemonic_v2('568-379-8466'):
    if i == 'LOVEPYTHON':
      print(i)