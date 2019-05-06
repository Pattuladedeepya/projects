def smallestmultiple(n):
  for i in range(n,factorial(n)+1,n):
    if ismultiple(i,n):
      return i
  return -1

def ismultiple(x,n):
  for i in range(1,n):
    if x % i != 0:
      return False
  return True

def factorial(n):
  if n>1:
    return n* factorial(n - 1)
  elif n >= 0:
    return 1
  else:
    return -1

print(smallestmultiple(20))
