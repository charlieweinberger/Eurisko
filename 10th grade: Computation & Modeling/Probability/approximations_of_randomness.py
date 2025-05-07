flips = {
    'Justin S': 'HTTH HHTT TTHH TTTH HHTH TTHT HHHH THHT THTT HTHH TTTT HTHT TTHH THTH HTTH HHTH HHHT TTTH HTTH HTHT',
    'Nathan R': 'HTTH HHTH HTTT HTHH HTTH HHHH TTHH TTHT THTT HTHT HHTH TTTT THHT HTTH HTHH THHH HTTH THTT HHHT HTHH',
    'Justin H': 'HHHT HHTH HHTT THHT HTTT HTTT HHHT HTTT TTTT HTHT THHH TTHT TTHH HTHT TTTT HHHH THHH THTH HHHH THHT',
    'Nathan A': 'HTTH HHHH THHH TTTH HTTT THTT HTHT THHT HTTH TTTT HHHH TTHH HHTH TTTH HHHH THTT HTHT TTTT HHTT HHTT',
    'Cayden': 'HTHT HHTT HTTH THTH THHT TTHH HHHH TTTH HHHT HTTT TTHT HHTH HTHH THTT HHHH THTT HTTT HTHH TTTT HTTH',
    'Maia': 'HTHH THTH HTTH TTTT TTHT HHHH HHTT THHH TTHH HHTH THHT HHHH THTT HHTH HTHT TTHH TTHH HHHH TTTT HHHT',
    'Spencer': 'HHHT HTTH HTTT HTHH THTT TTHT TTTT HTTH HHTH TTHT TTHH HTHT THHT TTHT THTT THTH HTTH THHT TTTH HHHH',
    'Charlie': 'HHHH HHHT HHTT HTTT TTTT TTTH TTHH THHH THTH HTHT HHTH HTHH TTHT THTT THTH TTHT HTHT THHT HTTH THTH',
    'Anton': 'HHTH THTH TTTT HTTH THTT TTTH THHH TTHH THHT HHHH TTHT HTTT THTH HHHT HHTH HHHH TTTH HTHT TTTT HHTT',
    'William': 'THTT HHHT HTTH THHT THTH HHHT TTTH HHTH THTH HTHT HHHT TTHT HHHT THTT HHTT TTHH HHTH TTTT THTH TTHT'
}

import math
from random import random

def factorial(n): 
    return 1 if n == 0 else n * factorial(n - 1)

def probability(h, f): 
    return (factorial(f) / (factorial(h) * factorial(f - h))) / (2 ** f)

def simulated_probability(num_heads, sample_list):
    correct_times = 0
    for sample in sample_list:
        actual_num_heads = 0
        for flip in sample:
            if flip == 'H':
                actual_num_heads += 1
        if actual_num_heads == num_heads:
            correct_times += 1

    return correct_times / len(sample_list)

def kl_divergence(p, q):
    ans = 0
    for n in range(len(p)):
        if p[n] and q[n] != 0:
            ans += p[n] * math.log(p[n] / q[n])
    return round(ans, 10)

def sort_dict(dictionary):
    ans_list = []
    dict_key_list = list(dictionary.keys())
    dict_value_list = list(dictionary.values())
    
    for i in range(len(dict_key_list)):

        value_index = dict_value_list.index(min(dict_value_list))
        smallest = [dict_key_list[value_index], dict_value_list[value_index]]
        ans_list.append(smallest)

        del dict_key_list[value_index]
        del dict_value_list[value_index]

    ans_dict = {}
    for item in ans_list:
        ans_dict[item[0]] = item[1]

    return ans_dict

def sorted_kl_divergence_dict(flips_dict):
    kl_divergence_dict = {}

    for name, all_samples in flips_dict.items():
        sample_list = all_samples.split(" ")
        flips_per_sample = len(sample_list[0])

        true_distribution = [probability(h, flips_per_sample) for h in range(flips_per_sample + 1)]
        simulation = [simulated_probability(h, sample_list) for h in range(flips_per_sample + 1)]
        kl_divergence_dict[name] = kl_divergence(simulation, true_distribution)

    return sort_dict(kl_divergence_dict)

answer = sorted_kl_divergence_dict(flips)

# part a
for key, value in answer.items():
    print("{}'s score: {}".format(key, value))

# part b
winner = list(answer.keys())[0]
print("\nWho won? {}!".format(winner))