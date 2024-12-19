def factorial(n):
  if n == 0: return 1
  if n < 0: return 'Error'
  return n * factorial(n - 1)

def perm(n, r):
  return factorial(n) / factorial(n - r)

def comb(n, r):
  return perm(n, r) / factorial(r)

print(comb(10, 2))