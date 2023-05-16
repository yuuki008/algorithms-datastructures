n = 6
A = [2, 3, 4, 5, 6, 7]


def is_prime_number(num) -> bool:
  if num <= 1:
    return False

  i = 2
  while i * i <= num:
    if num % i == 0:
      return False
    i += 1
  return True

ans = 0
for num in A:
  print(num)
  if is_prime_number(num):
    ans += 1
print(ans)