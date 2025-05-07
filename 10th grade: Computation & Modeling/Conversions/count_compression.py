# part a
def count_compression(string):
    ans = []
    for char_index in range(len(string)):
        char = string[char_index]
        if char == string[char_index - 1] and char_index != 0:
            ans[-1][1] += 1
        else:
            ans.append([char, 1])    
    return [tuple(group) for group in ans]

print("Testing count_compression('aaabbcaaaa')...")
assert count_compression('aaabbcaaaa') == [('a', 3), ('b', 2), ('c', 1), ('a', 4)], count_compression('aaabbcaaaa')
print("PASSED")

print("Testing count_compression('22344444')...")
assert count_compression('22344444') == [('2', 2), ('3', 1), ('4', 5)], count_compression('22344444')
print("PASSED")

# part b
def count_decompression(compressed_string):
    ans = ''
    for thing in compressed_string:
        for i in range(thing[1]):
            ans += str(thing[0])
    return ans

print("Testing count_decompression([('a',3), ('b',2), ('c',1), ('a',4)])...")
assert count_decompression([('a',3), ('b',2), ('c',1), ('a',4)]) == 'aaabbcaaaa', count_decompression([('a',3), ('b',2), ('c',1), ('a',4)])
print("PASSED")

print("Testing count_decompression([(2,2), (3,1), (4,5)])...")
assert count_decompression([(2,2), (3,1), (4,5)]) == '22344444', count_decompression([(2,2), (3,1), (4,5)])
print("PASSED")