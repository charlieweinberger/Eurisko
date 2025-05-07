edges = [('a','c'), ('e','g'), ('e','i'), ('e','a'), ('d','b'), ('a','d'), ('d','f'), ('f','h'), ('d','j'), ('d','k')]

def get_children(parent, tree):
    ans = [pair[1] for pair in tree if pair[0] == parent]
    return sorted(ans)
    
def get_parents(child, tree):
    ans = [pair[0] for pair in tree if pair[1] == child]
    return ans

def get_root(tree):
    childs = [pair[1] for pair in tree]
    ans = []
    for pair in tree:
        if (pair[0] not in childs) and (pair[0] not in ans):
            ans.append(pair[0])
    return ans

assert get_children('e', edges) == sorted(['a', 'i', 'g'])
assert get_children('c', edges) == []
assert get_children('f', edges) == ['h']

assert get_parents('e', edges) == []
assert get_parents('c', edges) == ['a']
assert get_parents('f', edges) == ['d']

assert get_root(edges) == ['e']

print("passed all tests")