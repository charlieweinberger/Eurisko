# sqrt(2) is in the interval [1,2]. We will estimate the value of sqrt(2) by repeatedly narrowing these bounds.

# part a
def update_bounds(bounds):

    a = bounds[0]
    b = bounds[1]
    halfway = (a + b) / 2
    new_bounds = []

    if halfway ** 2 > 2:
        return [a, halfway]
    else:
        return [halfway, b]

print('Testing update_bounds on input {}...'.format([1, 2]))
assert update_bounds([1, 2]) == [1, 1.5]
print("PASSED")

print('Testing update_bounds on input {}...'.format([1, 1.5]))
assert update_bounds([1, 1.5]) == [1.25, 1.5]
print("PASSED")

# part b
def estimate_root(precision, bounds):

    a = bounds[0]
    b = bounds[1]
    halfway = (a + b) / 2
    bounds = update_bounds(bounds)

    if (b - a) <= precision:
        return halfway
    else:
        return estimate_root(precision, bounds)

print("Testing estimate_root on inputs {}, {}...".format(0.1, [1, 2]))
assert estimate_root(0.1, [1, 2]) == 1.40625, "estimate_root(0.1, [1, 2]) == {}".format(estimate_root(0.1, [1, 2]))
print("PASSED")
