# python count_characters.py

def count_characters(input_string):
  ans = {}
  
  for char in input_string.lower():

    if str(char) not in ans.keys():
      ans[str(char)] = 1
    else:
      ans[str(char)] += 1

  return ans

print('Testing count_characters on the input {}...'.format('A cat!!!'))
assert count_characters('A cat!!!') == {'a': 2, 'c': 1, 't': 1, ' ': 1, '!': 3}
print('PASSED')