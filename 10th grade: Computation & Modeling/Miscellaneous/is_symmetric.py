# python is_symmetric.py

def is_symmetric(input_string):
  if input_string == input_string[::-1]:
    return True
  else:
    return False

print('Testing is_symmetric on input {}...'.format("racecar"))
assert is_symmetric("racecar") == True
print('PASSED')

print('Testing is_symmetric on input {}...'.format("batman"))
assert is_symmetric("batman") == False
print('PASSED')