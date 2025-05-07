from random import random

# 1. turn the distribution into a cumulative distribution
# 2. choose a random number between 0 and 1
# 3. find the index of the first value in the cumulative distribution that is greater than the random number.

def cumulative(distribution, i):
    if i == 0:
        return distribution[i]
    else:
        return distribution[i] + cumulative(distribution, i-1)

def random_draw(distribution):
    cumulative_distribution = [round(cumulative(distribution, i), 5) for i in range(len(distribution))]
    rand = random()
    for i in range(len(cumulative_distribution)):
        if cumulative_distribution[i] > rand:
            return i

def expected_value(distribution):
    ans = 0
    for i in range(len(distribution)):
        ans += distribution[i]*i
    return ans

def average(distribution, num_times):
    nums = [random_draw(distribution) for i in range(num_times)]
    return sum(nums) / len(nums)

print("\ndist 1:")
dist_1 = [0.5, 0.5]
print("expected_value:", expected_value(dist_1))
print("average calculated value:", average(dist_1, 10000))
error = round(abs(expected_value(dist_1) - average(dist_1, 10000)), 5)
print("error:", error)

print("\ndist 2:")
dist_2 = [0.25, 0.25, 0.5]
print("expected_value:", expected_value(dist_2))
print("average calculated value:", average(dist_2, 10000))
error = round(abs(expected_value(dist_2) - average(dist_2, 10000)), 5)
print("error:", error)

print("\ndist 3:")
dist_3 = [0.05, 0.2, 0.15, 0.3, 0.1, 0.2]
print("expected_value:", expected_value(dist_3))
print("average calculated value:", average(dist_3, 10000))
error = round(abs(expected_value(dist_3) - average(dist_3, 10000)), 5)
print("error:", error)

print("passed")