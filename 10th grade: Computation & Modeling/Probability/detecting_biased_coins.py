"""
Suppose that you run an experiment where you flip a coin 3 times, and repeat that trial 25 times. You run this experiment on 3 different coins.

Let Pi(x) be the experimental probability of getting x heads in a trial of 3 tosses, using the i th coin. Plot the distributions P1(x), P2(x), and P3(x) on the same graph. Be sure to label them.

This is similar to when you plotted the Monte Carlo distributions, but this time you're given the simulation results.

Based on the plot of the distributions, what conclusions can you make about the coins? For each coin, does it appear to be fair, biased towards heads, or biased towards tails? Write your answer as a comment.
"""

coin_1 = ['TTH', 'HHT', 'HTH', 'TTH', 'HTH',
          'TTH', 'TTH', 'TTH', 'THT', 'TTH',
          'HTH', 'HTH', 'TTT', 'HTH', 'HTH',
          'TTH', 'HTH', 'TTT', 'TTT', 'TTT',
          'HTT', 'THT', 'HHT', 'HTH', 'TTH']

coin_2 = ['HTH', 'HTH', 'HTT', 'THH', 'HHH',
          'THH', 'HHH', 'HHH', 'HTT', 'TTH',
          'TTH', 'HHT', 'TTH', 'HTH', 'HHT',
          'THT', 'THH', 'THT', 'TTH', 'TTT',
          'HHT', 'THH', 'THT', 'THT', 'TTT']

coin_3 = ['HHH', 'THT', 'HHT', 'HHT', 'HTH',
          'HHT', 'HHT', 'HHH', 'TTT', 'THH',
          'HHH', 'HHH', 'TTH', 'THH', 'THH',
          'TTH', 'HTT', 'TTH', 'HTT', 'HHT',
          'TTH', 'HTH', 'THT', 'THT', 'HTH']

import matplotlib.pyplot as plt
plt.style.use('bmh')

def odds(coin_list):

    num_heads_each_trial = []
    for trial in coin_list:
        num_h = 0
        for outcome in trial:
            if outcome == 'H':
                num_h += 1
        num_heads_each_trial.append(num_h)

    num_of_num_heads = [0, 0, 0, 0]
    for num in num_heads_each_trial:
        num_of_num_heads[num] += 1

    x_coords = [x for x in range(4)]
    y_coords = [num_of_num_heads[n]/len(coin_list) for n in range(4)]
    plt.plot(x_coords, y_coords)

odds(coin_1)
odds(coin_2)
odds(coin_3)

plt.legend(["coin_{}".format(n) for n in range(1, 4)])
plt.savefig('detecting_biased_coins.png')

"""

You can see that coin 1 is biased towards tails (lands more tails), coin_2 is not biased, and coin 3 is biased towards heads (lands more heads).

"""