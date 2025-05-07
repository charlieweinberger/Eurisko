def binary_search(entry, sorted_list):
    
    low = 0
    high = len(sorted_list) - 1
    
    while low != high:
        
        midpoint = (low + high) // 2
        midpoint_entry = sorted_list[midpoint]
        
        if entry < midpoint_entry:
            high = midpoint - 1
        elif entry > midpoint_entry:
            low = midpoint + 1
        else:
            return midpoint
    
    return low

assert binary_search(14, [2, 3, 5, 7, 8, 9, 10, 11, 13, 14, 15, 16]) == 9
assert binary_search(21, [5, 7, 9, 20, 21, 22, 23]) == 4

print("passed all")