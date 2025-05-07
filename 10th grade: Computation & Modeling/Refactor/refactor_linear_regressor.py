"""

Refactor this code so that it is more readable. It should be easy to glance at and understand what's going on. Some particular things to fix are:
- Putting whitespace where appropriate
- Naming variables clearly
- Expanding out complicated one-liners
- Deleting any pieces of code that aren't necessary

"""

def calculate_coefficients(self):
    final_dict = {}
    
    df_keys = list(self.df.data_dict.keys())
    df_values = list(self.df.data_dict.values())

    row_of_1s = [1 for _ in df_values[0]]
    mat_elements = [row_of_1s]

    for key in self.df.data_dict:
        if key != self.dependent_variable:
            observations = self.df.data_dict[key]
            mat_elements.append(observations)
    
    mat = Matrix(mat_elements)
    mat = mat.transpose()

    mat_t = mat.transpose()
    mat_mult = mat_t.matrix_multiply(mat)
    mat_inv = mat_mult.inverse()
    mat_pseudoinv = mat_inv.matrix_multiply(mat_t)
    
    y_elements = [[num] for num in df_values[1][0]]
    y = Matrix(y_elements)
    multiplier_mat = mat_pseudoinv.matrix_multiply(y)
    
    for num in range(len(multiplier_mat.elements)):
        if num == 0:
            key = 'constant'
        else:
            key = df_keys[num - 1]
      final_dict[key] = [row[0] for row in multiplier_mat.elements][num]
    
    return final_dict