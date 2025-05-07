class HashTable():

    def __init__(self, num_buckets):
        self.num_buckets = num_buckets
        self.buckets = [[] for _ in range(self.num_buckets)]
    
    def hash_function(self, string):
        
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        alphabet_dict = {alphabet[i]:i for i in range(len(alphabet))}
        
        total = 0
        for char in string:
            total += alphabet.index(char)
        
        return total % self.num_buckets
    
    def insert(self, key, value):
        pair = (key, value)
        bucket_index = self.hash_function(key)
        self.buckets[bucket_index].append(pair)
    
    def find(self, key):
        bucket_index = self.hash_function(key)
        for bucket in self.buckets:
            for pair in bucket:
                if pair[0] == key:
                    return pair[1]

print("Testing HashTable")

ht = HashTable(num_buckets = 3)
assert ht.buckets == [[], [], []]
assert ht.hash_function('cabbage') == 2 # (because 2 + 0 + 1 + 1 + 0 + 6 + 4 mod 3 = 14 mod 3 = 2)

ht.insert('cabbage', 5)
assert ht.buckets == [[], [], [('cabbage',5)]]

ht.insert('cab', 20)
assert ht.buckets == [[('cab', 20)], [], [('cabbage',5)]]

ht.insert('c', 17)
assert ht.buckets == [[('cab', 20)], [], [('cabbage',5), ('c',17)]]

ht.insert('ac', 21)
assert ht.buckets == [[('cab', 20)], [], [('cabbage',5), ('c',17), ('ac', 21)]]

assert ht.find('cabbage') == 5
assert ht.find('cab') == 20
assert ht.find('c') == 17
assert ht.find('ac') == 21

print("passed all")