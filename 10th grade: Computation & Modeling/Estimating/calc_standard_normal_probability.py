import math
import matplotlib.pyplot as plt
plt.style.use('bmh')

def f(x):
    return (math.e ** ((-(x ** 2)) / 2)) / ((2 * math.pi) ** (1/2))

def calc_standard_normal_probability(a, b, n, rule):
    ans = 0
    step_size = (b - a) / n
    points_sum = 0

    if rule == "left endpoint":
        for x in range(0, n):
            points_sum += f(a + (x * step_size))
    
    if rule == "right endpoint":
        for x in range(1, n + 1):
            points_sum += f(a + (x * step_size))
        
    if rule == "midpoint":
        for x in range(0, n):
            points_sum += f((2*a + (2*x + 1)*step_size) / 2)
    
    if rule == "trapezoidal":
        for x in range(1, n):
            points_sum += f(a + (x * step_size))
        points_sum += (f(a) + f(b)) / 2
    
    if rule == "simpson":
        index = 0
        for num in range(1, n):
            if index % 2 == 0:
                points_sum += 4 * f(a + num * step_size)
            elif index % 2 == 1:
                points_sum += 2 * f(a + num * step_size)
            index += 1

        points_sum += f(a) + f(b)
        points_sum /= 3
    
    return step_size * points_sum

n_points = [2*i for i in range(1, 51)]
left = [calc_standard_normal_probability(0, 1, n, "left endpoint") for n in n_points]
right = [calc_standard_normal_probability(0, 1, n, "right endpoint") for n in n_points]
mid = [calc_standard_normal_probability(0, 1, n, "midpoint") for n in n_points]
trapezoidal = [calc_standard_normal_probability(0, 1, n, "trapezoidal") for n in n_points]
simpson = [calc_standard_normal_probability(0, 1, n, "simpson") for n in n_points]

plt.plot(n_points, left, label="Left riemann sum")
plt.plot(n_points, right, label="Right riemann sum")
plt.plot(n_points, mid, label="Midpoint riemann sum")
plt.plot(n_points, trapezoidal, label="Trapezoidal riemann sum")
plt.plot(n_points, simpson, label="Simpson riemann sum")

plt.xlabel('n')
plt.ylabel('P(0 < x < 1)')
plt.legend(loc="upper right")
plt.title('Estimated value of P(0 < x < 1) for n going from 2 to 100')
plt.savefig('calc_standard_normal_probability.png')