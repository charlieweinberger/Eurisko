# part a
def identity_matrix_elements(n):
    return [[1 if col_num == row_num else 0 for col_num in range(n)] for row_num in range(n)]

print("Testing identity_matrix_elements(4)...")
ans1 = [[1, 0, 0, 0],
       [0, 1, 0, 0],
       [0, 0, 1, 0],
       [0, 0, 0, 1]]
assert identity_matrix_elements(4) == ans1
print("PASSED")

# part b
def counting_across_rows_matrix_elements(m, n):
    return [[(4 * row_num) + col_num + 1 for col_num in range(n)] for row_num in range(m)]

print("Testing counting_across_rows_matrix_elements(3, 4)...")
ans2 = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12]]
assert counting_across_rows_matrix_elements(3, 4) == ans2, counting_across_rows_matrix_elements(3, 4)
print("PASSED")