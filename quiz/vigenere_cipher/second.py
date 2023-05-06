import string

def generate_key(message: str, keyword: str) -> str:
  key = keyword
  remain_length = len(message) - len(keyword)
  for i in range(remain_length):
    key += key[i]
  return key

def vigenere_cipher_v1(text: str, key: str) -> str:
  len_alphabet = ord('Z') - ord('A') + 1
  result = ''
  for i in range(len(text)):
    if text[i].isupper():
      alphabet = string.ascii_uppercase
    elif text[i].islower():
      alphabet = string.ascii_lowercase
    else:
      result += text[i]
      continue

    index = alphabet.index(text[i]) + alphabet.index(key[i])

    if index > len_alphabet:
      index = index % len_alphabet
    result += alphabet[index]
  return result

def vigenere_cipher_hack_v1(text: str, key: str) -> str:
  len_alphabet = ord('Z') - ord('A') + 1
  result = ''
  for i in range(len(text)):
    if text[i].isupper():
      alphabet = string.ascii_uppercase
    elif text[i].islower():
      alphabet = string.ascii_lowercase
    else:
      result += text[i]
      continue

    index = alphabet.index(text[i]) - alphabet.index(key[i])
    if index < 0:
      index += len_alphabet
    result += alphabet[index]
  return result

if __name__ == '__main__':
  print(generate_key('ABCDEF', 'CAT'))
  # text = 'ABCDZ'
  # key = 'HELLO'
  # encrypted = vigenere_cipher_v1(text, key)
  # print(encrypted)
  # decrypted = vigenere_cipher_hack_v1(encrypted, key)
  # print(decrypted)
