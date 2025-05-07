# python is_prime.py

def is_prime(n):
  ans = True
  for divisor in range(n):
    if (divisor != 0 and divisor != 1 and divisor != n): 
      for whole_num in range(101):
          if n/divisor == whole_num:
            ans = False
  return ans

print('Testing is_prime on input {}...'.format(59))
assert is_prime(59) == True
print('PASSED')

print('Testing is_prime on input {}...'.format(51))
assert is_prime(51) == False
print('PASSED')