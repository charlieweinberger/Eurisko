# python convert_to_base_10.py

def convert_to_base_10(binary_num):

    binary_array = []
    for num in str(binary_num):
        binary_array.append(num)

    int_binary_array = []
    for num2 in binary_array:
        int_binary_array.append(int(num2))

    opposite_of_nums_to_zero = []
    for num3 in range(len(int_binary_array)):
        opposite_of_nums_to_zero.append(num3)
    nums_to_zero = opposite_of_nums_to_zero[::-1]

    decimal_num = 0
    for num4 in range(len(int_binary_array)):
        decimal_num += int_binary_array[num4] * (2 ** nums_to_zero[num4])
  
    return decimal_num

print('Testing convert_to_base_10 on the input {}...'.format(10011))
assert convert_to_base_10(10011) == 19
print('PASSED')