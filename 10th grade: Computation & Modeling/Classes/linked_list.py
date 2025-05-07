class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.index = 0

class LinkedList():
    def __init__(self, head):
        self.head = Node(head)
    
    def print_data(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next
    
    def length(self):
        current_node = self.head
        length = 0
        while current_node is not None:
            length += 1
            current_node = current_node.next 
        return length
    
    def append(self, new_data):
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = Node(new_data)
        current_node.next.index = self.length() - 1
    
    def push(self, new_data):
        new_linked_list = LinkedList(new_data)
      
        current_node = self.head
        while current_node is not None:
            new_linked_list.append(current_node.data)
            current_node = current_node.next

        current_node = self.head
        current_new_node = new_linked_list.head
        while current_node is not None:
            current_node.data = current_new_node.data
            current_node.index = current_new_node.index
            current_node = current_node.next
            current_new_node = current_new_node.next
        
        self.append(new_linked_list.get_node(new_linked_list.length() - 1).data)

    def get_node(self, index):
        current_node = self.head
        while current_node.index < index:
            current_node = current_node.next 
        return current_node
    
    def delete(self, index):
        new_linked_list = LinkedList(self.head.data)

        current_node = self.head.next
        while current_node is not None:
            if current_node.index != index:
                new_linked_list.append(current_node.data)
            current_node = current_node.next

        current_node = self.head
        current_new_node = new_linked_list.head
        while current_node.next is not None:
            if current_node.index > index + 1:
                current_node.index -= 1
            current_node.data = current_new_node.data
            current_node = current_node.next
            current_new_node = current_new_node.next

        self.get_node(self.length() - 2).next = None
    
    def insert(self, new_data, index):
        new_linked_list = LinkedList(self.head.data)

        current_node = self.head.next
        while current_node is not None:
            if current_node.index == index:
                new_linked_list.append(new_data)
            new_linked_list.append(current_node.data)
            current_node = current_node.next

        current_node = self.head
        current_new_node = new_linked_list.head
        while current_new_node.next is not None:
            current_node.data = current_new_node.data
            current_node = current_node.next
            current_new_node = current_new_node.next
        
        self.append(new_linked_list.get_node(new_linked_list.length() - 1).data)

print("\nAssignment 16-2")

A = Node(4)
B = Node(8)

assert A.data == 4
assert A.next == None

A.next = B
assert A.next.data == 8

linked_list = LinkedList(4)
linked_list.append(8)
linked_list.append(9)

# linked_list.print_data()
assert linked_list.head.data == 4
assert linked_list.head.next.data == 8
assert linked_list.length() == 3

print("passed Assignment 16-2")

print("\nAssignment 18-2")

linked_list = LinkedList('b')
linked_list.append('e')
linked_list.append('f')
linked_list.push('a')

assert linked_list.length() == 4, linked_list.length()

assert linked_list.head.index == 0, linked_list.head.index
assert linked_list.head.next.index == 1, linked_list.head.next.index
assert linked_list.head.next.next.index == 2, linked_list.head.next.next.index
assert linked_list.head.next.next.next.index == 3, linked_list.head.next.next.next.index

assert linked_list.get_node(0).data == 'a'
assert linked_list.get_node(1).data == 'b'
assert linked_list.get_node(2).data == 'e'
assert linked_list.get_node(3).data == 'f'

print("passed Assignment 18-2")

print("\nAssignment 20-2")

linked_list = LinkedList('a')
linked_list.append('b')
linked_list.append('c')
linked_list.append('d')
linked_list.append('e')
assert linked_list.length() == 5
# linked_list.print_data()

assert linked_list.get_node(2).data == 'c'
linked_list.delete(2)
assert linked_list.length() == 4, linked_list.length()
assert linked_list.get_node(2).data == 'd'
linked_list.print_data()

linked_list.insert('f', 2)
assert linked_list.length() == 5, linked_list.length()
assert linked_list.get_node(2).data == 'f', linked_list.get_node(2).data
# linked_list.print_data()

print("passed Assignment 20-2")