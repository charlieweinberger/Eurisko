def factorial(n): return 1 if n == 0 else n * factorial(n-1)

def probability(h, f):  return factorial(f) / ((2 ** f) * (factorial(h) * factorial(f - h)))

print("Testing probability(5,8)...")
assert probability(5, 8) == 0.21875, probability(5, 8)
print("PASSED")

# part b
from random import random

def monte_carlo_probability(num_heads, num_flips):
    outcomes = [[['h', 't'][round(random())] for flips in range(num_flips)] for num in range(1000)]

    times_it_was_correct = 0
    for outcome in outcomes:
        actual_num_heads = 0
        for result in outcome:
            if result == 'h':
                actual_num_heads += 1
        if actual_num_heads == num_heads:
            times_it_was_correct += 1

    return times_it_was_correct / 1000

# part c
print(monte_carlo_probability(5, 8))
print(monte_carlo_probability(5, 8))
print(monte_carlo_probability(5, 8))
print(monte_carlo_probability(5, 8))
print(monte_carlo_probability(5, 8))