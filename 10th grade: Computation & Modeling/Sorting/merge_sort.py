def merge(x, y):
    ans = []
    for i in range(len(x + y)):
        x_min = min(x) if len(x) > 0 else 100000000
        y_min = min(y) if len(y) > 0 else 100000000
        minimum = x_min if x_min < y_min else y_min
        current_list = x if minimum == x_min else y
        ans.append(minimum)
        del current_list[current_list.index(minimum)]
    return ans

print("Testing merge...")
assert merge([-2,1,4,4,4,5,7], [-1,6,6]) == [-2,-1,1,4,4,4,5,6,6,7], merge([-2,1,4,4,4,5,7], [-1,6,6])
print("passed")

def merge_sort(input_list):
    if len(input_list) > 1:
        left = input_list[0:len(input_list)//2]
        right = input_list[len(input_list)//2:len(input_list)]
        sorted_left = merge_sort(left)
        sorted_right = merge_sort(right)
        return merge(sorted_left, sorted_right)
    else:
        return input_list

print("Testing merge_sort...")
assert merge_sort([4, 8, 7, 7, 4, 2, 3, 1]) == [1, 2, 3, 4, 4, 7, 7, 8], merge_sort([4, 8, 7, 7, 4, 2, 3, 1])
print("passed")