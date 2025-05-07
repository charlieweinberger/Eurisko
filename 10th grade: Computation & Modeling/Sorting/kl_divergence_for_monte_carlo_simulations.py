import math
from random import random

def factorial(n): return 1 if n == 0 else n * factorial(n - 1)

def monte_carlo_probability(num_heads, num_flips, num_samples):
    outcomes = [[['h', 't'][round(random())] for flips in range(num_flips)] for num in range(num_samples)]

    times_it_was_correct = 0
    for outcome in outcomes:
        actual_num_heads = 0
        for result in outcome:
            if result == 'h':
                actual_num_heads += 1
        if actual_num_heads == num_heads:
            times_it_was_correct += 1

    return times_it_was_correct / num_samples

# part a
def kl_divergence(p, q):
    ans = 0
    for n in range(len(p)):
        if p[n] and q[n] != 0:
            ans += p[n] * math.log(p[n] / q[n])
    return round(ans, 6)

p = [0.2, 0.5, 0, 0.3]
q = [0.1, 0.8, 0.1, 0]

print("Testing kl_divergence(p, q) where p = {} and q = {}".format(p, q))
assert kl_divergence(p, q) == -0.096372
print("PASSED")

# part b
def kl_divergence_for_mc_sims(s):
    p = [monte_carlo_probability(h, 8, s) for h in range(9)]
    q = [157.5 / (factorial(h) * factorial(8 - h)) for h in range(9)]
    return kl_divergence(p, q)

print("Computing KL Divergence for MC Simulations...")
print("100 samples --> KL Divergence = {}".format(kl_divergence_for_mc_sims(100)))
print("1,000 samples --> KL Divergence = {}".format(kl_divergence_for_mc_sims(1000)))
print("10,000 samples --> KL Divergence = {}".format(kl_divergence_for_mc_sims(10000)))

# part c
# As the number of samples increases, the KL divergence approaches 0. As the number of samples increases, the simlated probability gets closer and closer to the actual probability. This means p gets closer to q, which means that p[n] gets closer to q[n] for all n, which means that p[n] / q[n] gets closer to 1, which means that ln(p[n] / q[n]) gets closer to ln(1), or 0. So as the number of samples increased, the KL divergence approaches 0.