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

ans3 = cartesian_product([[1, 2], ['a', 'b', 'c'], [76]])
print(ans3)

assert cartesian_product([['a'], [1, 2, 3], ['Y', 'Z']]) == [['a',1,'Y'], ['a',1,'Z'], ['a',2,'Y'], ['a',2,'Z'], ['a',3,'Y'], ['a',3,'Z']]
print("passed")