def is_list_valid(row):
    return all([row.count(elem) == 1 for elem in row if elem != None])

def grid_to_rows(grid):
    rows = []
    row = []
    for i in range(len(grid)):
        if i % n_by_n == n_by_n - 1:
            rows.append(row + [grid[i]])
            row = []
        else:
            row.append(grid[i])
    return rows

def grid_to_subgrids(grid):
    new_grid = grid_to_rows(grid)
    subgrids = []
    for l in range(0, n_by_n, num_subgrid_rows):
        for k in range(0, num_subgrid_cols + 1, num_subgrid_cols):
            subgrid = []
            for j in range(num_subgrid_rows):
                for i in range(num_subgrid_cols):
                    elem = new_grid[j + l][i + k]
                    subgrid.append(elem)
            subgrids.append(subgrid)
    return subgrids

def is_valid(grid):

    for elem in grid:
        if elem not in list(range(1, n_by_n + 1)) and elem != None:
            return False

    rows = grid_to_rows(grid)
    columns = [[row[i] for row in rows] for i in range(n_by_n)]
    subgrids = grid_to_subgrids(grid)

    return all([is_list_valid(elem) for elem in rows + columns + subgrids])

def find_sudoku(grid):

    index = 0
    move_forward = True
    known_elems_indices = [n for n in range(len(grid)) if grid[n] != None]

    while None in grid or not is_valid(grid):

        if index in known_elems_indices:
            if move_forward:
                index += 1
            else:
                index -= 1

        else:

            if grid[index] == None:
                grid[index] = 0
            grid[index] += 1
            
            if grid[index] > n_by_n:
                grid[index] = None
                index -= 1
                move_forward = False
                continue

            if is_valid(grid):
                index += 1
                move_forward = True

    return grid

num_subgrid_rows = 2
num_subgrid_cols = 3
n_by_n = num_subgrid_rows * num_subgrid_cols

grid = [None, None,    4, None, None, None,
        None, None, None,    2,    3, None,
           3, None, None, None,    6, None,
        None,    6, None, None, None,    2,
        None,    2,    1, None, None, None,
       None, None, None,    5, None, None]

new_grid = grid_to_rows(find_sudoku(grid))
str_ans = ''

for i in range(6):
    row = new_grid[i]
    if i % 2 == 0:
        str_ans += '\n-----------------'
    str_ans += '\n| ' + str(row[0:3])[1:-1].replace(',', '') + ' | ' + str(row[3:6])[1:-1].replace(',', '') + ' |'

str_ans += '\n-----------------'

print(str_ans)