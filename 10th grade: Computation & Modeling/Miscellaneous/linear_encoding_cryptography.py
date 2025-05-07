# python Assignment4/linear_encoding_cryptography.py

# part a
def encode(string, a, b):

    trivial_encoding = []
    for char in string:
        if char == " ":
            trivial_encoding.append(0)
        else:
            for char2 in range(26):
                if char == chr(char2 + 97):
                    trivial_encoding.append(char2 + 1)

    linear_encoding = []
    for num in trivial_encoding:
        linear_encoding.append((a * num) + b)
    return linear_encoding

print("\npart a:")
print('Testing encode on input {}...'.format('a cat', 2, 3))
assert encode('a cat', 2, 3) == [5, 3, 9, 5, 43], "encode('a cat', 2, 3) == {}".format(encode('a cat', 2, 3))
print("PASSED")

# part b
def decode(numbers, a, b):
    ans = ""
    for num in numbers:
        decoded_number = (num - b) / a
        
        integer_part = int(str(decoded_number).split('.')[0])
        decimal_part = int(str(decoded_number).split('.')[1])
        if not 0 <= integer_part <= 26 or decimal_part != 0:
            return False
        
        if integer_part == 0:
            ans += " "
        else:
            ans += chr(integer_part + 96)

    return ans

print("\npart b:")
print('Testing decode on input {}...'.format([5, 3, 9, 5, 43], 2, 3))
assert decode([5, 3, 9, 5, 43], 2, 3) == 'a cat'
print("PASSED")

print('Testing decode on input {}...'.format([1, 3, 9, 5, 43], 2, 3))
assert decode([1, 3, 9, 5, 43], 2, 3) == False
print("PASSED")

print('Testing decode on input {}...'.format([5, 3, 9, 5, 44], 2, 3))
assert decode([5, 3, 9, 5, 44], 2, 3) == False
print("PASSED")

# part c
def part_c(encoded_message):
    ans_array = []
    for a in range(1, 100):
        for b in range(0, 100):
            this_ans = ""
            for encoded_num in encoded_message:
                decoded_num = (encoded_num - b) / a
                
                integer_part = int(str(decoded_num).split('.')[0])
                decimal_part = int(str(decoded_num).split('.')[1])
                if not 0 <= integer_part <= 26 or decimal_part != 0:
                    break
        
                if integer_part == 0:
                    this_ans += " "
                else:
                    this_ans += chr(integer_part + 96)
            
            if this_ans != '' and len(this_ans) > 2:
                ans_array.append(this_ans)
    
    ans = ""
    for ans_string in ans_array:
        ans += ans_string + "\n"
    
    return ans
    

print("\npart c:")
print(part_c([377, 717, 71, 513, 105, 921, 581, 547, 547, 105, 377, 717, 241, 71, 105, 547, 71, 377, 547, 717, 751, 683, 785, 513, 241, 547, 751]))