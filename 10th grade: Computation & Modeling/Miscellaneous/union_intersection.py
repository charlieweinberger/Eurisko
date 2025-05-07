# python union_intersection.py

# part a
def intersection(list_1, list_2):
  ans = []
  for char_1 in list_1:
    for char_2 in list_2:
      if char_1 == char_2:
        ans.append(char_1)
  return ans

print('Testing intersection on inputs {} and {}...'.format([1,2,'a','b'], [2,3,'a']))
assert intersection([1,2,'a','b'], [2,3,'a']) == [2,'a'], 'desired output {} but actual output {}'.format([2,'a'], intersection([1,2,'a','b'], [2,3,'a']))
print('PASSED')

# part b
def union(list_1, list_2):

  nums_in_list_1 = []
  lets_in_list_1 = []
  for char_1 in list_1:
    if str(char_1).isdigit() == True:
      nums_in_list_1.append(char_1)
    else:
      lets_in_list_1.append(char_1)

  nums_in_list_2 = []
  lets_in_list_2 = []
  for char_2 in list_2:
    if str(char_2).isdigit() == True:
      nums_in_list_2.append(char_2)
    else:
      lets_in_list_2.append(char_2)

  # union of nums
  all_nums = []
  all_nums = nums_in_list_1
  for num_1 in nums_in_list_2:
    new_num = True
    for num_2 in nums_in_list_1:
      if num_1 == num_2:
        new_num = False
    if new_num == True:
      all_nums.append(num_1) 
  union_of_nums = sorted(all_nums)

  # union of lets
  all_lets = []
  all_lets = lets_in_list_1
  for let_1 in lets_in_list_2:
    new_let = True
    for let_2 in lets_in_list_1:
      if let_1 == let_2:
        new_let = False
    if new_let == True:
      all_lets.append(let_1)
  union_of_lets = sorted(all_lets)

  #add them together
  final_union = union_of_nums + union_of_lets
  return final_union

print('Testing union on inputs {} and {}...'.format([1,2,'a','b'], [2,3,'a']))
assert union([1,2,'a','b'], [2,3,'a']) == [1,2,3,'a','b'], 'desired output {} but actual output {}'.format([1,2,3,'a','b'], union([1,2,'a','b'], [2,3,'a']))
print('PASSED')

print("HERE NOW")
ans = union([1,2,'a','b'], [2,3,'a'])