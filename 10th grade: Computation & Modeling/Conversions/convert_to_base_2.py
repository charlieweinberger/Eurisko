import math

def convert_to_base_2(decimal_num):

    binary_array = []
    length_of_binary_num = math.ceil(math.log(decimal_num) / math.log(2))
    
    for num in range(1, length_of_binary_num + 1):
        num_to_zero = length_of_binary_num - num

        if (2 ** (num_to_zero + 1)) > decimal_num and (2 ** (num_to_zero)) <= decimal_num:
            binary_array.append(1)
            decimal_num -= (2 ** (num_to_zero))
        else:
            binary_array.append(0)
    
    binary_num = ""
    for num in binary_array:
        binary_num += str(num)

    return int(binary_num)

print('Testing convert_to_base_2 on input {}...'.format(19))
assert convert_to_base_2(19) == 10011
print("PASSED")