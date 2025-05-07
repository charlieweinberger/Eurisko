minimum = 68
power = 4
num_times = 10000
percent_goal = 0.95

def sigma(a, b, c):
    ans = 0
    for i in range(a, b + 1):
        ans += p(i, c)
    return ans

def p(k, c):
    return 0 if k < minimum else c / (k ** power)

def percent_sure(c, minimum, num_times, percent_goal):

    for k in range(minimum, num_times):
        ans = sigma(minimum, k, c)
        if ans >= percent_goal:
            return k

def do_problem(minimum, num_times, percent_goal):
    c = 1 / sigma(1, num_times, 1)
    print("c =", c)

    ans = percent_sure(c, minimum, num_times, percent_goal)
    return ans

final_ans = do_problem(minimum, num_times, percent_goal)
print("I can be {}% sure that the upper bound is less than".format(percent_goal), final_ans)