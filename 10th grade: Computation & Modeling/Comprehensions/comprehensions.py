# part a
def even_odd_tuples(num_list):
    return [(num, 'even') if num % 2 == 0 else (num, 'odd') for num in num_list]

print("Testing even_odd_tuples on input {}...".format([1, 2, 3, 5, 8, 11]))
assert even_odd_tuples([1, 2, 3, 5, 8, 11]) == [(1,'odd'), (2,'even'), (3,'odd'), (5,'odd'), (8,'even'), (11,'odd')]
print("PASSED")

# part b
def even_odd_dict(num_list):
    return{num: 'even' if num % 2 == 0 else 'odd' for num in num_list}

correct_answer = {
    1:'odd',
    2:'even',
    3:'odd',
    5:'odd',
    8:'even',
    11:'odd'
}

print("Testing even_odd_dict on input {}...".format([1, 2, 3, 5, 8, 11]))
assert even_odd_dict([1, 2, 3, 5, 8, 11]) == correct_answer
print("PASSED")