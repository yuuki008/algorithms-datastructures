import heapq
from typing import List
from collections import Counter


def top_n_with_heap(words: List[str], n: int) -> List[str]:
  counter_word = Counter(words)
  data = [(-counter_word[word], word) for word in counter_word]
  heapq.heapify(data)
  return [heapq.heappop(data)[1] for _ in range(n)]

if __name__ == '__main__':
  w =['python', 'c', 'java', 'go', 'python', 'c', 'go', 'python']
  print(top_n_with_heap(w, 3))

