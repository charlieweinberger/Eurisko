def parse_value(string):
    if string[0] == '"' and string[-1] == '"':
            return string.strip('"')
        elif '.' in string:
            return float(string)
        else:
            return int(string)

test_string = '"alpha","beta","gamma","delta"\n1,2,3,4\n5.0,6.0,7.0,8.0'

def string_processor(test_string):
    split_test_string = test_string.split('\n')
    split_test_string_list = [x.split(',') for x in split_test_string]

    ans = []
    for value_list in split_test_string_list:
        parsed_values = [parse_value(elem) for elem in value_list]
        ans.append(parsed_values)
    
    return ans 

print(string_processor(test_string))