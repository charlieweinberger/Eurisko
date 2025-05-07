def is_list_valid(row):
    return not (None not in row and sum(row) != 15)

def is_valid(arr):
    
    # rows
    valid_row_list = [is_list_valid(row) for row in arr]
    all_rows_valid = all(valid_row_list)

    # columns
    columns = [[row[i] for row in arr] for i in range(3)]
    valid_column_list = [is_list_valid(column) for column in columns]
    all_columns_valid = all(valid_column_list)

    # diagonals
    left_to_right_diagonal = [arr[i][i] for i in range(3)]
    right_to_left_diagonal = [arr[i][2 - i] for i in range(3)]
    diagonals = [left_to_right_diagonal, right_to_left_diagonal]

    valid_diagonal_list = [is_list_valid(diagonal) for diagonal in diagonals]
    all_diagonals_valid = all(valid_diagonal_list)
    
    all_valid_list = [all_rows_valid, all_columns_valid, all_diagonals_valid]
    return all(all_valid_list)

def clear_and_insert(nums):
    arr = [[None for _ in range(3)] for _ in range(3)]
    nums = [nums[i] if i < len(nums) else None for i in range(9)]
    
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            arr[i][j] = nums[3*i + j]

    return arr

def find_magic_square():
    arr = [[None for _ in range(3)] for _ in range(3)]

    for num1 in range(1,10):
        
        arr = clear_and_insert([num1])
        if not is_valid(arr):
            continue
        
        for num2 in range(1,10):

            if num2 != num1:
                arr = clear_and_insert([num1, num2])
                if not is_valid(arr):
                    continue
            
                for num3 in range(1,10):

                    if num3 not in [num1, num2]:
                        arr = clear_and_insert([num1, num2, num3])
                        if not is_valid(arr):
                            continue
                
                        for num4 in range(1,10):

                            if num4 not in [num1, num2, num3]:
                                arr = clear_and_insert([num1, num2, num3, num4])
                                if not is_valid(arr):
                                    continue
                
                                for num5 in range(1,10):

                                    if num5 not in [num1, num2, num3, num4]:
                                        print("\nlist:", [num1, num2, num3, num4, num5])
                                        arr = clear_and_insert([num1, num2, num3, num4, num5])
                                        print("arr :", arr)
                                        quit()
                                        
                                        if not is_valid(arr):
                                            continue
                                        
                                        for num6 in range(1,10):

                                            if num6 not in [num1, num2, num3, num4, num5]:
                                                arr = clear_and_insert([num1, num2, num3, num4, num5, num6])
                                                if not is_valid(arr):
                                                    continue
                                                
                                                for num7 in range(1,10):

                                                    if num7 not in [num1, num2, num3, num4, num5, num6]:
                                                        arr = clear_and_insert([num1, num2, num3, num4, num5, num6, num7])
                                                        if not is_valid(arr):
                                                            continue
                                                        
                                                        for num8 in range(1,10):

                                                            if num8 not in [num1, num2, num3, num4, num5, num6, num7]:
                                                                arr = clear_and_insert([num1, num2, num3, num4, num5, num6, num7, num8])
                                                                if not is_valid(arr):
                                                                    continue
                                                                
                                                                for num9 in range(1,10):

                                                                    if num9 not in [num1, num2, num3, num4, num5, num6, num7, num8]:
                                                                        arr = clear_and_insert([num1, num2, num3, num4, num5, num6, num7, num8, num9])
                                                                        if not is_valid(arr):
                                                                            continue
                                                                        return arr

print(find_magic_square())