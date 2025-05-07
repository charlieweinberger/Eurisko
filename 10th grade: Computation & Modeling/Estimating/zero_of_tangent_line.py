def f(x):
    return x**3 + x - 1

def zero_of_tangent_line(f, c, delta):
    m = estimate_derivative(f, c, delta)
    return c - f(c)/m

def estimate_solution(f, initial_guess, precision):
    x_list = [initial_guess, zero_of_tangent_line(f, initial_guess, 0.001)]
    difference = abs(x_list[-2] - x_list[-1])

    while precision < difference:
        x_list.append(zero_of_tangent_line(f, x_list[-1], 0.001))
        difference = abs(x_list[-2] - x_list[-1])
    
    return x_list[-1]

def estimate_derivative(f, c, delta):
    return (f(c + 0.5*delta) - f(c - 0.5*delta)) / delta

def f(x):
    return 1 - x**2

"""
print("Testing zero_of_tangent_line(f, 0.5)...")
answer = zero_of_tangent_line(f, 0.5, 0.001)
assert round(answer, 6) == 0.714286, round(answer, 6)
print("passed")

print("Testing estimate_solution(f, 0.5, 0.01)...")
answer = estimate_solution(f, 0.5, 0.01)
assert round(answer, 6) == 0.682328, round(answer, 6)
print("passed")
"""