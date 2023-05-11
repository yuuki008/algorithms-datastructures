def main(line: str):
  LOC = []
  POOL = []
  sum = 0
  for i in range(len(line)):
    if line[i] == '\\':
      LOC.append(i)
    elif line[i] == '/':
      if len(LOC) == 0:
        continue

      j = LOC.pop()
      temp_area = i - j
      sum += temp_area
      while len(POOL) > 0 and POOL[-1][0] > j:
        temp_area += POOL.pop()[1]
      POOL.append((j, temp_area))

  print(sum)
  if len(POOL) == 0:
    print(len(POOL))
  else:
    print(len(POOL), end=' ')
    for i in range(len(POOL)-1):
      print(POOL[i][1], end=' ')
    print(POOL[-1][1])

if __name__ == "__main__":
  main("""\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\""")