# Write a function that takes the cartesian product of the grid_lines in the search space, evaluates the objective_function at all points of intersection, and returns the point where the objective_function takes the lowest value.

def cartesian_product(arrays):
    
    ans = arrays[0]
    for i in range(1, len(arrays)):
        ans = [[a, b] for a in ans for b in arrays[i]]

    str_ans_without_brackets = "["
    for char in [char for char in str(ans) if char != "[" and char != "]"]:
        str_ans_without_brackets += char
    str_ans_without_brackets += "]"

    answer = str_ans_without_brackets.split(",")

    for elem_index in range(len(answer)):
        temp = ""
        for char in answer[elem_index]:
            if char != "\'" and char != "\"" and char != "[" and char != "]" and char != " ":
                temp += char
        answer[elem_index] = temp

    numbers = [str(num) for num in range(0, 10)] + ["."]
    for elem_index in range(len(answer)):
        is_num = True
        for char in answer[elem_index]:
            if char not in numbers:
                is_num = False
        if is_num:
            answer[elem_index] = float(answer[elem_index])

    real_ans = []
    for elem_index in range(len(answer) // len(arrays)):
        real_ans.append([answer[len(arrays) * elem_index + i] for i in range(len(arrays))])
    
    return real_ans

def grid_search(objective_function, grid_lines):

    intersections = cartesian_product(grid_lines)
    y_list = [two_variable_function(pair[0], pair[1]) for pair in intersections]

    for pair in intersections:
        if two_variable_function(pair[0], pair[1]) == min(y_list):
            return pair

def two_variable_function(x, y):
    return (x**2)*(y**2) + 2*((y - 1)**2)

x_lines = [0, 1]
y_lines = [0, 1, 2]
grid_lines = [x_lines, y_lines]

print(grid_search(two_variable_function, grid_lines))

"""
# tests
def two_variable_function(x, y):
    return (x - 1) ** 2 + (y - 1) ** 3

x_lines = [0, 0.25, 0.75]
y_lines = [0.9, 1, 1.1, 1.2]
grid_lines = [x_lines, y_lines]

assert grid_search(two_variable_function, grid_lines) == [0.75, 0.9]
print("passed")
"""