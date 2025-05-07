# python stack.py

class Stack():
    def __init__(self):
        self.data = []

    def push(self, string):
        self.data.append(string)
        
    def pop(self):
        del self.data[-1]
        
    def peek(self):
        return self.data[-1]

s = Stack()

print("Asserting that s.data == {}".format([]))
assert s.data == []
print("PASSED")

s.push('a')
s.push('b')
s.push('c')

print("Asserting that s.data == {}".format(['a', 'b', 'c']))
assert s.data == ['a', 'b', 'c']
print("PASSED")

s.pop()

print("Asserting that s.data == {}".format(['a', 'b']))
assert s.data == ['a', 'b']
print("PASSED")

print("Asserting that s.peek == {}".format('b'))
assert s.peek() == 'b'
print("PASSED")

print("Asserting that s.data == {}".format(['a', 'b']))
assert s.data == ['a', 'b']
print("PASSED")