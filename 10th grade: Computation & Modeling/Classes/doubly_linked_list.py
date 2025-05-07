class Node():
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None
        self.index = 0

class DoublyLinkedList():
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
        current_node.next.prev = current_node
        current_node.next.index = self.length() - 1
    
    def push(self, new_data):
        new_doubly_linked_list = LinkedList(new_data)
      
        current_node = self.head
        while current_node is not None:
            new_doubly_linked_list.append(current_node.data)
            current_node = current_node.next

        current_node = self.head
        current_new_node = new_doubly_linked_list.head
        while current_node is not None:
            current_node.data = current_new_node.data
            current_node.index = current_new_node.index
            current_node = current_node.next
            current_new_node = current_new_node.next
        
        self.append(new_doubly_linked_list.get_node(new_doubly_linked_list.length() - 1).data)

    def get_node(self, index):
        current_node = self.head
        while current_node.index < index:
            current_node = current_node.next 
        return current_node
    
    def delete(self, index):
        new_doubly_linked_list = DoublyLinkedList(self.head.data)

        current_node = self.head.next
        while current_node is not None:
            if current_node.index != index:
                new_doubly_linked_list.append(current_node.data)
            current_node = current_node.next

        current_node = self.head
        current_new_node = new_doubly_linked_list.head
        while current_node.next is not None:
            if current_node.index > index + 1:
                current_node.index -= 1
            current_node.data = current_new_node.data
            current_node = current_node.next
            current_new_node = current_new_node.next

        self.get_node(self.length() - 2).next = None
    
    def insert(self, new_data, index):
        new_doubly_linked_list = DoublyLinkedList(self.head.data)

        current_node = self.head.next
        while current_node is not None:
            if current_node.index == index:
                new_doubly_linked_list.append(new_data)
            new_doubly_linked_list.append(current_node.data)
            current_node = current_node.next

        current_node = self.head
        current_new_node = new_doubly_linked_list.head
        while current_new_node.next is not None:
            current_node.data = current_new_node.data
            current_node = current_node.next
            current_new_node = current_new_node.next
        
        self.append(new_doubly_linked_list.get_node(new_doubly_linked_list.length() - 1).data)

print("\nTesting Assignment 30-2")

doubly_linked_list = DoublyLinkedList('a')
doubly_linked_list.append('c')
doubly_linked_list.append('d')
doubly_linked_list.append('e')
doubly_linked_list.insert('b',1)
doubly_linked_list.delete(3)

current_node = doubly_linked_list.get_node(3)
node_values = [current_node.data]

for _ in range(3):
    current_node = current_node.prev
    node_values.append(current_node.data)

assert node_values == ['e', 'c', 'b', 'a'], node_values

print("Passed Assignment 30-2")