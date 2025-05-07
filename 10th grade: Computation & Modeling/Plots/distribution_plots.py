from random import random

def factorial(n):
    if n == 0:
      return 1
    else:
      return n * factorial(n-1)

def probability(h, f):
    return factorial(f) / ((2 ** f) * (factorial(h) * factorial(f - h)))

def monte_carlo_probability(h, f):
    outcomes = [[['h', 't'][round(random())] for flips in range(f)] for num in range(1000)]

    times_it_was_correct = 0
    for outcome in outcomes:
        actual_h = 0
        for result in outcome:
            if result == 'h':
                actual_h += 1
        if actual_h == h:
            times_it_was_correct += 1

    return times_it_was_correct / 1000

"""
import matplotlib.pyplot as plt
plt.style.use('bmh')

total_lines = 6
num_flips = 8

true_distribution_list = [[probability(y, num_flips) for y in range(num_flips + 1)]]
MC_list = [[monte_carlo_probability(y, num_flips) for y in range(num_flips + 1)], [monte_carlo_probability(y, num_flips) for y in range(num_flips + 1)], [monte_carlo_probability(y, num_flips) for y in range(num_flips + 1)], [monte_carlo_probability(y, num_flips) for y in range(num_flips + 1)], [monte_carlo_probability(y, num_flips) for y in range(num_flips + 1)], [monte_carlo_probability(y, num_flips) for y in range(num_flips + 1)]]

x_coords = [x for x in range(num_flips + 1)]
y_coords = true_distribution_list + MC_list

plt.plot(x_coords, y_coords[0], linewidth = 2.5)
for num in range(1, total_lines):
    plt.plot(x_coords, y_coords[num], linewidth = 0.75)

plt.legend(['True'] + ["MC {}".format(num) for num in range(1, total_lines)])
plt.xlabel('Number of Heads')
plt.ylabel('Probability')
plt.title('True Distribution vs Monte Carlo Simulations for 8 Coin Flips')
plt.savefig('plot.png')
"""

import matplotlib.pyplot as plt
plt.style.use('bmh')

total_lines = 6
num_flips = 8

true_distribution_list = [probability(y, num_flips) for y in range(num_flips + 1)]
MC_list = [monte_carlo_probability(y, num_flips) for y in range(num_flips + 1)]

n = 5

x_coords = [[num for num in range(n)], [num for num in range(n)]]
y_coords = true_distribution_list + MC_list

plt.plot(x_coords, y_coords[0], linewidth = 2.5)
for num in range(1, total_lines):
    plt.plot(x_coords, y_coords[num], linewidth = 0.75)

plt.legend(['True'] + ["MC {}".format(num) for num in range(1, total_lines)])
plt.xlabel('Number of Heads')
plt.ylabel('Probability')
plt.title('True Distribution vs Monte Carlo Simulations for 8 Coin Flips')
plt.savefig('plot.png')