# python Assignment4/flatten.py

# NOTE: 'animal' and 'food' are not dictionaries

def flatten(nested_dict):
    flat_dict = {}
    for key in nested_dict:
        for small_key, small_value in nested_dict[key].items():
            flat_dict[str(key) + '_' + str(small_key)] = small_value
    return flat_dict

colors = {
  'animal': {
    'bumblebee': ['yellow', 'black'],
    'elephant': ['gray'],
    'fox': ['orange', 'white']
  },
  'food': {
    'apple': ['red', 'green', 'yellow'],
    'cheese': ['white', 'orange']
  }
}

correct_ans = {
  'animal_bumblebee': ['yellow', 'black'],
  'animal_elephant': ['gray'],
  'animal_fox': ['orange', 'white'],
  'food_apple': ['red', 'green', 'yellow'],
  'food_cheese': ['white', 'orange']
}

print('Testing flatten on the input{}...\n'.format(colors))
assert flatten(colors) == correct_ans
print("PASSED")