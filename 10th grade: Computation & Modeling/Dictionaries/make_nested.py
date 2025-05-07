# python make_nested.py

def make_nested(flat_dictionary):
    ans = {}
    for key, value in flat_dictionary.items():
        # key = classification_thing
        classification = key.split('_')[0]
        thing = key.split('_')[1]
        if classification not in ans:
            ans[str(classification)] = {thing: value} 
        else:
            ans[str(classification)][str(thing)] = value
    return ans

print('Testing make_nested on the input{}...\n'.format(colors))
assert make_nested(colors) == {
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
print("PASSED")
