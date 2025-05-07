class DataFrame():
    
    def __init__(self, data_dict, columns):
        self.data_dict = data_dict
        self.columns = columns
        self.column_values = list(self.data_dict.values())

        self.num_rows = len(self.column_values)
        self.num_cols = len(self.column_values[0])
    
    def copy(self):
        return DataFrame(self.data_dict, self.columns)
    
    def to_array(self):
        c = self.copy()

        ans = [[0 for num2 in range(c.num_rows)] for num in range(c.num_cols)]
                
        for m in range(c.num_cols):
            for n in range(c.num_rows):
                ans[m][n] = c.column_values[n][m]
        
        return ans
    
    def select(self, name_list):
        c = self.copy()

        dict_ans = {}
        for name in name_list:
            for key, value in c.data_dict.items():
                if name == key:
                    dict_ans[name] = value

        return DataFrame(dict_ans, list(dict_ans.keys()))
    
    def select_rows(self, row_indices):
        c = self.copy()

        dict_ans = {}
        for key, value in c.data_dict.items():
            dict_ans[key] = [value[index] for index in range(len(value)) if index in row_indices]

        return DataFrame(dict_ans, list(dict_ans.keys()))
    
    def apply(self, name, f):
        c = self.copy()

        row = []
        for key, value in c.data_dict.items():
            if key == name:
                row = value
        
        row = [f(n) for n in row]
        c.data_dict[name] = row

        return c
    
    def convert_row_from_array_to_dict(self, arr):
        c = self.copy()

        dict_ans = {c.columns[elem_index]:arr[elem_index] for elem_index in range(len(arr))}

        return dict_ans

    def query(self, string):
        
        string = string.replace(',', '').split(' ')
        better_string = []
        for elem in string:
            if elem not in ['ORDER', 'BY']:
                better_string.append(elem)
            elif elem == 'ORDER':
                better_string.append('ORDER BY')
                continue
                
        operations = [elem for elem in better_string if elem in ['SELECT', 'ORDER BY']]

        operations_and_column_names = []
        new_list = [operations[0]]

        for elem in better_string[1:]:
            
            if elem in operations:
                operations_and_column_names.append(new_list)
                new_list = [elem]
            else:
                new_list.append(elem)
        
        operations_and_column_names.append(new_list)
        
        better_operations_and_column_names = [] 
        for arr in operations_and_column_names:
            
            if arr[0] == 'ORDER BY':
                new_arr = ['ORDER BY']

                for j in range(len(arr[1:]) // 2):
                    new_elem = [arr[1:][2*j], arr[1:][2*j + 1]]
                    new_arr.append(new_elem)
            
                better_operations_and_column_names.append(new_arr)
            
            else:
                better_operations_and_column_names.append(arr)

        for pair in better_operations_and_column_names[1][1:][::-1]: 
            self = self.order_by(pair[0], pair[1] == 'ASC')

        self = self.select(better_operations_and_column_names[0][1:])
        self.columns = list(self.data_dict)

        return self

    def where(self, f):
        c = self.copy()

        dict_ans = {c.columns[index]:[] for index in range(len(c.columns))}

        people_dict_list = [c.convert_row_from_array_to_dict(person) for person in c.to_array()]
        
        for person_dict in people_dict_list:
            if f(person_dict):
                for key, value in person_dict.items():
                    dict_ans[key].append(value)
        
        return DataFrame(dict_ans, c.columns) 
    
    def order_by(self, this_key, ascending=True):
        c = self.copy()

        people_dict_list = [c.convert_row_from_array_to_dict(person) for person in c.to_array()]
        people_dict_list.sort(reverse = not ascending, key = lambda row: row[this_key])

        values = [list(person_dict.values()) for person_dict in people_dict_list]

        dict_ans = {c.columns[index]:[] for index in range(len(c.columns))}

        for key_index in range(len(c.columns)):
            for person_list in values:
                dict_ans[c.columns[key_index]].append(person_list[key_index])

        return DataFrame(dict_ans, c.columns)

    def group_by(self, this_key):
        c = self.copy()

        key_list = c.data_dict[this_key]
        
        non_repeating_key_list = []
        for key in key_list:
            if key not in non_repeating_key_list:
                non_repeating_key_list.append(key)
        
        part_ans = [[[] for _ in non_repeating_key_list] for key in c.data_dict if key != this_key]

        for elem1 in non_repeating_key_list:
            for i in range(len(key_list)):
                
                if elem1 == key_list[i]:
                    
                    for key in c.data_dict:
                        
                        if key != this_key:
                                
                            value_list = c.data_dict[key]
                            value = value_list[i]

                             # only works when this_key is the first key in c.columns
                            j = c.columns.index(key) - 1
                            k = non_repeating_key_list.index(key_list[i])
                            part_ans[j][k].append(value)

        # only works when this_key is the first key in c.columns
        data_dict = {}
        for i in range(len(c.columns)):
            
            current_key = c.columns[i]

            if current_key == this_key:
                data_dict[current_key] = non_repeating_key_list
            else:
                data_dict[current_key] = part_ans[i - 1]

        ans_list = [[data_dict[key][i] for key in c.columns] for i in range(len(non_repeating_key_list))]

        return DataFrame.from_array(ans_list, c.columns)
    
    def aggregate(self, colname, how):
        c = self.copy()

        for i in range(len(c.data_dict[colname])):

            if how == 'count':
                c.data_dict[colname][i] = len(c.data_dict[colname][i])
            
            elif how == 'max':
                c.data_dict[colname][i] = max(c.data_dict[colname][i])
            
            elif how == 'min':
                c.data_dict[colname][i] = min(c.data_dict[colname][i])
            
            elif how == 'sum':
                c.data_dict[colname][i] = sum(c.data_dict[colname][i])
            
            elif how == 'avg':
                c.data_dict[colname][i] = sum(c.data_dict[colname][i]) / len(c.data_dict[colname][i])

        return c

    @classmethod
    def from_array(cls, arr, columns):
        
        dict_ans = {}        
        for thing in columns:
            dict_ans[thing] = []

        index = 0
        for key, value in dict_ans.items():
            value += [person[index] for person in arr]
            index += 1

        return DataFrame(dict_ans, columns)

    @classmethod
    def from_csv(cls, path_to_csv, header=True, data_types=None, parser=None):
        
        with open(path_to_csv, "r") as file:
            
            file_str = file.read()
            big_list = file_str.split("\n")

            arrays = [string.split(",  ") for string in big_list]
            arrays = [arrays[1:len(arrays)]][0]
            arrays = [elem for elem in arrays if elem != ['']]

            columns = big_list[0].split(", ")
            if parser != None:
                columns = parser(columns[0])

            for i in range(len(arrays)):
                arrays[i] = parser(arrays[i][0])

            for i in range(len(arrays)):

                new_arr = []
                for j in range(len(arrays[i])):

                    data_type = list(data_types.values())[j]
                    old_value = arrays[i][j]
                    
                    if old_value == '':
                        new_value = None
                    else:
                        new_value = data_type(old_value)

                    new_arr.append(new_value)
                
                arrays[i] = new_arr

            return DataFrame.from_array(arrays, columns)
    
    def create_interaction_terms(self, dependent_variable):
        
        dependent_variable_index = self.columns.index(dependent_variable)
        dependent_variable_value = self.data_dict[dependent_variable]
        del self.data_dict[dependent_variable]
        del self.columns[dependent_variable_index]

        new_columns = []
        for i in range(len(self.columns)):
            for j in range(len(self.columns)):
                if i < j:
                    new_column = self.columns[i] + ' * ' + self.columns[j]
                    new_columns.append(new_column)
        self.columns += new_columns
        
        for i in range(len(self.columns)):
            
            key_string = self.columns[i]
            key_list = key_string.split(' * ')

            value_list = []
            for j in range(len(self.column_values[0])):
                value = 1
                for key in key_list:
                    value *= self.data_dict[key][j]
                value_list.append(value)
            
            self.data_dict[key_string] = value_list

        self.data_dict[dependent_variable] = dependent_variable_value
        
        self.column_values = list(self.data_dict.values())
        self.num_rows = len(self.column_values)
        self.num_cols = len(self.column_values[0])

        return self
    
    def create_dummy_variables(self, column_name):
        column_index = self.columns.index(column_name)
        column_list = self.column_values[column_index]
        
        # only works if one of the elements in column_list has all the condiments.
        condiment_keys_lengths = [len(elem) for elem in column_list]
        for len_index in range(len(condiment_keys_lengths)):
            if condiment_keys_lengths[len_index] == max(condiment_keys_lengths):
                condiments = column_list[len_index]

        columns = self.columns
        del columns[column_index]
        for condiment in condiments[::-1]:
            columns.insert(column_index, condiment)

        numbers_list = []
        for elem in column_list:
            
            to_add = [0 for _ in range(len(condiments))]
            for condiment in elem:
                
                for n in range(len(condiments)):
                    if condiment == condiments[n]:
                        to_add[n] = 1

            numbers_list.append(to_add)
        
        column_values = self.column_values
        del column_values[column_index]
        all_condiment_nums = [[thing[n] for thing in numbers_list] for n in range(column_index)]
        for thing in all_condiment_nums[::-1]:
            column_values.insert(column_index, thing)

        data_dict = {}
        for i in range(len(column_values)):
            key = columns[i]
            value = column_values[i]
            data_dict[key] = value

        return DataFrame(data_dict, columns)