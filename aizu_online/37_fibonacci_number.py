n = 40
dp = [None for _ in range(n+1)]

def fib(n):
  if dp[n]:
    return dp[n]
  if n <= 1:
    return 1

  dp[n] = fib(n-1) + fib(n-2)
  return dp[n]

print(fib(n))