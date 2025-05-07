class Queue():
    def __init__(self):
        self.data = []

    def enqueue(self, item):
        self.data.append(item)
        
    def dequeue(self):
        del self.data[0]
        
    def peek(self):
        return self.data[0]

q = Queue()

print("Asserting that q.data == {}".format([]))
assert q.data == []
print("PASSED")

q.enqueue('a')
q.enqueue('b')
q.enqueue('c')

print("Asserting that q.data == {}".format(['a', 'b', 'c']))
assert q.data == ['a', 'b', 'c']
print("PASSED")

q.dequeue()

print("Asserting that q.data == {}".format(['b', 'c']))
assert q.data == ['b', 'c']
print("PASSED")

print("Asserting that q.peek == {}".format('b'))
assert q.peek() == 'b'
print("PASSED")

print("Asserting that q.data == {}".format(['b', 'c']))
assert q.data == ['b', 'c']
print("PASSED")