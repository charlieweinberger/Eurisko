# part a
def unlist_nonrecursive(x):
    if type(x) == list:
        while len(x) == 1:
            if type(x[0]) == list:
                x = x[0]
            else:
                return x[0]
    return x

print("Testing unlist_nonrecursive([[[[1], [2,3], 4]]])...")
problem_1 = [[[[1], [2,3], 4]]]
ans_1 = [[1], [2,3], 4]
assert unlist_nonrecursive(problem_1) == ans_1, unlist_nonrecursive(problem_1)
print("PASSED")

print("Testing unlist_nonrecursive([[[[1]]]])...")
assert unlist_nonrecursive([[[[1]]]]) == 1, unlist_nonrecursive([[[[1]]]])
print("PASSED")

# part b
def unlist_recursive(x):
    if type(x) == list:
        if len(x) == 1:
            return unlist_recursive(x[0])
        else:
          return x
    else:
        return x

print("Testing unlist_recursive([[[[1], [2,3], 4]]])...")
problem_2 = [[[[1], [2,3], 4]]]
ans_2 = [[1], [2,3], 4]
assert unlist_recursive(problem_2) == ans_2, unlist_recursive(problem_2)
print("PASSED")

print("Testing unlist_recursive([[[[1]]]])...")
assert unlist_recursive([[[[1]]]]) == 1, unlist_recursive([[[[1]]]])
print("PASSED")