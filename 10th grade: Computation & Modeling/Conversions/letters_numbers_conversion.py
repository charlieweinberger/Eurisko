# python letters_numbers_conversion.py

def convert_to_numbers(input_string):
  array_ans = []
  for char in input_string:
    if char == " ":
      array_ans.append(0)
    else:
      for char2 in range(26):
        if char == chr(char2 + 97):
          array_ans.append(char2 + 1)
  return array_ans

def convert_to_letters(input):
  ans = ""
  for num in input:
    if num == 0:
      ans += " "
    else:
      ans += chr(num + 96)
  return ans

print('Testing convert_to_numbers on input {}...'.format('a cat'))
assert convert_to_numbers('a cat') == [1, 0, 3, 1, 20], 'desired output {} but actual output {}'.format([1, 0, 3, 1, 20], convert_to_numbers('a cat'))
print('PASSED')

print('Testing convert_to_letters on input {}...'.format([1,0,3,1,20]))
assert convert_to_letters([1, 0, 3, 1, 20]) == 'a cat', 'desired output {} but actual output {}'.format('a cat', convert_to_letters([1,0,3,1,20]))
print('PASSED')