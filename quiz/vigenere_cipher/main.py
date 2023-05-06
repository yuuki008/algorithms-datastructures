import string

ALPHABET = string.ascii_uppercase

def generate_key(message: str, keyword: str) -> str:
  key = keyword
  remain_length = len(message) - len(keyword)
  for i in range(remain_length):
    key += key[i]
  return key

def encrypt(message: str, key: str) -> str:
  result = ''
  # len_alphabet = len(ALPHABET)
  len_alphabet = ord('Z') - ord('A') + 1
  for i, char in enumerate(message):
    if char not in ALPHABET:
      result += char
      continue
    # index = (ALPHABET.index(char) + ALPHABET.index(key[i])) % len(ALPHABET)
    index = (ord(char) - ord('A') + ord(key[i]) - ord('A')) % len_alphabet
    result += ALPHABET[index]
  return result

def decrypt(message: str, key: str) -> str:
  result = ''
  for i, char in enumerate(message):
    if char not in ALPHABET:
      result += char
      continue

    index = (ALPHABET.index(char) - ALPHABET.index(key[i])) + len(ALPHABET) % len(ALPHABET)
    result += ALPHABET[index]

  return result


if __name__ == "__main__":
  message = 'ATTACK SILICON VALLEY'
  keyword = 'CAT'
  key = generate_key(message, keyword)
  print(key)
  encrypted = encrypt(message, key)
  print(encrypted)
  decrypted = decrypt(encrypted, key)
  print(decrypted)
  if message == decrypted:
    print('SUCCESS')
  else:
    print("FAILURE")
