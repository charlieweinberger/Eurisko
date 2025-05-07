def minimum(num_list):
    smallest_num = num_list[0]
    for num in num_list:
        if smallest_num > num:
            smallest_num = num
    return smallest_num

# For any given list, the number of pairs of elements (that need to be compared by each algorithm) is exactly the same.

def simple_sort(num_list):
    ans = []
    for i in range(len(num_list)):
        ans.append(minimum(num_list))
        del num_list[num_list.index(minimum(num_list))]
    return ans

print("Testing simple_sort([5,8,2,2,4,3,0,2,-5,3.14,2])...")
assert simple_sort([5,8,2,2,4,3,0,2,-5,3.14,2]) == [-5,0,2,2,2,2,3,3.14,4,5,8], simple_sort([5,8,2,2,4,3,0,2,-5,3.14,2])
print("PASSED")

def swap_sort(num_list):
    for this_thing in num_list:
        for index in range(len(num_list) - 1):
            if num_list[index] > num_list[index + 1]:
                num_list[index], num_list[index + 1] = num_list[index + 1], num_list[index]
    return num_list

print("Testing swap_sort([5,8,2,2,4,3,0,2,-5,3.14,2])...")
assert swap_sort([5,8,2,2,4,3,0,2,-5,3.14,2]) == [-5,0,2,2,2,2,3,3.14,4,5,8]
print("PASSED")